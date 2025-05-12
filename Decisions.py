import random
import asyncio
from enum import Enum, auto
from datetime import datetime
from typing import Optional, Dict, Any
import sys
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor
import time  # Добавлен импорт time


class DecisionStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    DECIDED = auto()


class AnimatedProgress:
    def __init__(self):
        self.frames = cycle(["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"])
        self.current_frame = next(self.frames)
        self.message = ""
        self.progress = 0

    def update(self):
        self.current_frame = next(self.frames)
        self.progress = min(100, self.progress + random.randint(1, 5))
        return (
            f"\r{self.current_frame} {self.message.ljust(30)} "
            f"[{'█' * (self.progress // 2)}{' ' * (50 - self.progress // 2)}] "
            f"{self.progress}%"
        )


class DecisionMetrics:
    def __init__(self):
        self._factors: Dict[str, float] = {
            'weather': random.uniform(0, 1),
            'mood': random.uniform(0, 1),
            'finance': random.uniform(0, 1),
            'energy': random.uniform(0, 1),
            'opportunity': random.uniform(0, 1),
            'traffic': random.uniform(0, 1),
            'luck': random.uniform(0, 1)
        }
        self._weights: Dict[str, float] = {
            'weather': 0.25,
            'mood': 0.2,
            'finance': 0.15,
            'energy': 0.1,
            'opportunity': 0.1,
            'traffic': 0.1,
            'luck': 0.1
        }
        self._dynamic_values = {
            'weather': ["☀️ Sunny", "🌧️ Rainy", "⛅ Cloudy", "🌪️ Stormy"],
            'mood': ["😊 Happy", "😐 Neutral", "😞 Sad", "🤩 Excited"],
            'energy': ["⚡ High", "🔋 Medium", "🪫 Low"],
        }

    def calculate_score(self) -> float:
        return sum(
            self._factors[factor] * self._weights[factor]
            for factor in self._factors
        )

    def get_dynamic_factor(self, factor: str) -> str:
        if factor in self._dynamic_values:
            index = int(self._factors[factor] * (len(self._dynamic_values[factor]) - 1))
            return self._dynamic_values[factor][index]
        return f"{self._factors[factor]:.2f}"

    def update_factors(self):
        for factor in self._factors:
            self._factors[factor] = min(1, max(0, self._factors[factor] + random.uniform(-0.1, 0.1)))


class DecisionLogger:
    @staticmethod
    def log_decision(decision: str, metrics: DecisionMetrics) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 60)
        print(f"🚀 FINAL DECISION: {'GO ✈️' if decision == 'GO' else 'STAY 🏠'}")
        print("=" * 60)
        print("📊 Decision Factors Analysis:")
        for factor, value in metrics._factors.items():
            print(f"  - {factor.capitalize().ljust(10)}: {metrics.get_dynamic_factor(factor)} "
                  f"(weight: {metrics._weights[factor]:.2f})")
        print(f"\n🔍 Total score: {metrics.calculate_score():.2f}")
        print(f"⏱️ Decision timestamp: {timestamp}")
        print("=" * 60)


class DecisionEngine:
    def __init__(self):
        self._status = DecisionStatus.PENDING
        self._metrics = DecisionMetrics()
        self._decision: Optional[str] = None
        self._progress = AnimatedProgress()

    async def _update_progress(self):
        messages = [
            "Analyzing weather patterns",
            "Checking mood levels",
            "Scanning financial status",
            "Measuring energy reserves",
            "Evaluating opportunities",
            "Calculating traffic conditions",
            "Consulting the universe"
        ]

        while self._status == DecisionStatus.PROCESSING:
            self._progress.message = random.choice(messages)
            sys.stdout.write(self._progress.update())
            sys.stdout.flush()
            self._metrics.update_factors()
            await asyncio.sleep(0.1)

    async def analyze(self) -> None:
        self._status = DecisionStatus.PROCESSING

        # Запускаем обновление прогресса параллельно с анализом
        progress_task = asyncio.create_task(self._update_progress())

        # Имитация сложных асинхронных вычислений
        with ThreadPoolExecutor() as executor:
            await asyncio.get_event_loop().run_in_executor(
                executor, lambda: [time.sleep(0.05) for _ in range(100)]
            )

        score = self._metrics.calculate_score()
        self._decision = "GO" if score > 0.5 else "STAY"
        self._status = DecisionStatus.DECIDED

        # Даем прогресс-бару завершиться
        await asyncio.sleep(0.2)
        progress_task.cancel()
        sys.stdout.write("\r" + " " * 100 + "\r")
        sys.stdout.flush()

    def get_decision(self) -> str:  # Добавлен отсутствующий метод
        if self._status != DecisionStatus.DECIDED:
            raise RuntimeError("Decision not made yet")
        return self._decision

    def get_status(self) -> DecisionStatus:
        return self._status


def decision_decorator(func):
    async def wrapper(*args, **kwargs):
        print("\n🚦 Starting Advanced Decision Matrix v3.0")
        print("🔧 Initializing quantum decision engine...\n")
        await asyncio.sleep(1)
        result = await func(*args, **kwargs)
        print("\n⚡ Decision engine shutdown complete")
        return result

    return wrapper


class TripDecider:
    @decision_decorator
    async def make_decision(self) -> str:
        engine = DecisionEngine()
        await engine.analyze()
        decision = engine.get_decision()
        DecisionLogger.log_decision(decision, engine._metrics)
        return decision


async def main():
    decider = TripDecider()
    decision = await decider.make_decision()

    # Дополнительная анимация после принятия решения
    for _ in range(5):
        for frame in ["⢀", "⢂", "⢎", "⢰", "⢠", "⢈", "⢉", "⢙", "⢹", "⢪", "⢫"]:
            print(f"\rProcessing consequences {frame}", end="")
            await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(main())