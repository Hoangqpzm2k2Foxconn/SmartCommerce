
from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    def process_payment(self, amount, currency):
        pass
    
    @abstractmethod
    def verify_payment(self, payment_id):
        pass

class PaymentService:
    def __init__(self, provider: PaymentProvider):
        self.provider = provider
    
    def create_payment(self, amount, currency):
        return self.provider.process_payment(amount, currency)
    
    def verify_transaction(self, payment_id):
        return self.provider.verify_payment(payment_id)
