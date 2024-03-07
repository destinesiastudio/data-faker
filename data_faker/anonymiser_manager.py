from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer
from uuid import uuid5, UUID, NAMESPACE_DNS

class AnonymiserManager:
    mapping = {}

    def add(self, id: UUID, text: str):
        if id in self.mapping.keys():
            anonymiser = self.mapping[id]
        else:
            anonymiser = PresidioReversibleAnonymizer(
                analyzed_fields=['PERSON', 'EMAIL_ADDRESS', 'PHONE_NUMBER', 'IBAN_CODE', 'CREDIT_CARD', 'CRYPTO', 'IP_ADDRESS', 'LOCATION', 'NRP', 'MEDICAL_LICENSE', 'URL', 'US_BANK_NUMBER', 'US_DRIVER_LICENSE', 'US_ITIN', 'US_PASSPORT', 'US_SSN']
            )
            id = uuid5(NAMESPACE_DNS, 'destinesiastudio.com.au')
            self.mapping[id] = anonymiser

        anon_text = anonymiser.anonymize(text, language="en")

        return anon_text, id
    
    def revert(self, id: UUID, text: str) -> str:
        if id in self.mapping.keys():
            anonymiser: PresidioReversibleAnonymizer = self.mapping[id]
            deanon_text = anonymiser.deanonymize(text)

            return deanon_text
        
    def clear(self, id: UUID) -> bool:
        if id in self.mapping.keys():
            del self.mapping[id]
            return True
        
        return False