import json
import logging
from dataclasses import dataclass, field
from time import perf_counter


logger = logging.getLogger(__name__)


@dataclass
class ChatTiming:
    """Collect structured latency and count data for one chat request."""

    request_id: str
    durations_ms: dict[str, float] = field(default_factory=dict)
    openai_call_durations_ms: list[float] = field(default_factory=list)
    tool_call_durations_ms: list[float] = field(default_factory=list)
    tool_call_count: int = 0
    retrieved_document_count: int = 0
    rag_context_size_chars: int = 0

    def measure(self, stage: str):
        return _StageTimer(self, stage)

    def record_openai_call(self, duration_ms: float) -> None:
        duration_ms = round(duration_ms, 2)
        call_number = len(self.openai_call_durations_ms) + 1
        self.openai_call_durations_ms.append(duration_ms)
        self._log_event(
            event="chat_openai_call_timing",
            call_number=call_number,
            duration_ms=duration_ms,
        )

    def record_tool_call(self, duration_ms: float) -> None:
        duration_ms = round(duration_ms, 2)
        self.tool_call_count += 1
        self.tool_call_durations_ms.append(duration_ms)
        self._log_event(
            event="chat_tool_timing",
            call_number=self.tool_call_count,
            duration_ms=duration_ms,
        )

    def _log_event(self, **payload: object) -> None:
        logger.info(
            "%s",
            json.dumps(
                {
                    "request_id": self.request_id,
                    **payload,
                },
                sort_keys=True,
            ),
        )

    def log_summary(self, total_duration_ms: float) -> None:
        payload = {
            "event": "chat_timing",
            "request_id": self.request_id,
            "total_request_ms": round(total_duration_ms, 2),
            "durations_ms": {
                **self.durations_ms,
                "generation": round(
                    self.durations_ms.get("generation", 0.0),
                    2,
                ),
            },
            "openai_call_count": len(self.openai_call_durations_ms),
            "openai_call_durations_ms": [
                round(duration, 2)
                for duration in self.openai_call_durations_ms
            ],
            "tool_call_count": self.tool_call_count,
            "tool_call_durations_ms": [
                round(duration, 2)
                for duration in self.tool_call_durations_ms
            ],
            "retrieved_document_count": self.retrieved_document_count,
            "rag_context_size_chars": self.rag_context_size_chars,
        }
        self._log_event(**payload)


class _StageTimer:
    def __init__(self, timing: ChatTiming, stage: str) -> None:
        self._timing = timing
        self._stage = stage
        self._started_at = 0.0

    def __enter__(self):
        self._started_at = perf_counter()
        return self

    def __exit__(self, _exception_type, _exception_value, _traceback):
        duration_ms = round(
            (perf_counter() - self._started_at) * 1000,
            2,
        )
        self._timing.durations_ms[self._stage] = duration_ms
        self._timing._log_event(
            event="chat_stage_timing",
            stage=self._stage,
            duration_ms=duration_ms,
        )