from abc import ABC, abstractmethod


class Repository[T](ABC):
    @abstractmethod
    async def get_all(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    async def add(self, **kwargs: object) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: int, **kwargs: object) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> None:
        raise NotImplementedError
