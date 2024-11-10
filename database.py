from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class Database(ABC):
    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass
    
    @abstractmethod
    def get(self, id: int) -> Optional[Dict]:
        pass
    
    @abstractmethod
    def create(self, item: Dict) -> Dict:
        pass
    
    @abstractmethod
    def update(self, id: int, item: Dict) -> Optional[Dict]:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
