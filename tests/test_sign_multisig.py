from bitcoin_client.common import AddressType
from bitcoin_client.psbt import PSBT

def test_sign_multisig(cmd):
    # legacy address

    unsigned_raw_psbt_base64 = "cHNidP8BAH0CAAAAAQ5HHvTpLBrLUe/IZg+NP2mTbqnJsr/3L/m8gcUe/PRkAQAAAAD9////ArmoOwAAAAAAFgAUNcbg3W08hLFrqIXcpzrIY9C1k+xwEQEAAAAAACIAIP3uRBxW5bBtDfgsEkxwcBSlyhlli+C5hWvKFvHtMln3AAAAAAABAIgCAAAAAZXf7wah/zeZl5w2fzI91OWHTXbYoKMhQy721zey6JUvAAAAABcWABSPsnHXGKDY3oyXy+y9qkU7T0ui6/7///8CEPdqqQEAAAAWABRO796NdCbgG+W8qJf2alrndA2/ZsO6PAAAAAAAFgAUE0foKgN7Xbs4z4xHWfJCsfXH4JrEGB4AAQEfw7o8AAAAAAAWABQTR+gqA3tduzjPjEdZ8kKx9cfgmiIGAny3XTSwBcTrn2K78sRX12OOgT51fvzsj6aGd9lQtjZiGPWswv1UAACAAQAAgAAAAIAAAAAAAAAAAAAiAgJxtbd5rYcIOFh3l7z28MeuxavnanCdck9I0uJs+HTwoBj1rML9VAAAgAEAAIAAAACAAQAAAAAAAAAAAA=="
    psbt = PSBT()
    psbt.deserialize(unsigned_raw_psbt_base64)

    