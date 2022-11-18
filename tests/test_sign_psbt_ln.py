
from bitcoin_client.ledger_bitcoin import Client, WalletPolicy

from test_utils import has_automation


@has_automation("automations/sign_with_wallet_accept.json")
def test_sign_psbt_ln(client: Client):

    print("FINGERPRINT:", client.get_master_fingerprint())

    wallet = WalletPolicy(
        "",
        "wpkh(@0/**)",
        [
            "[f5acc2fd/84'/1'/0']tpubDCtKfsNyRhULjZ9XMS4VKKtVcPdVDi8MKUbcSD9MJDyjRu1A2ND5MiipozyyspBT9bg8upEp7a8EAgFxNxXn1d7QkdbL52Ty5jiSLcxPt1P"
        ],
    )

    psbt = 'cHNidP8BAIcCAAAAAvstuFuqt+tUKfzDJVVDkd1lrONmrkr9N/b31gfRN+oUAAAAAAD9////2+2WlTPf5hz0lcS2je0hwyutH1kxzcn75Ae1ZePYKMgAAAAAAP3///8BbGwEAAAAAAAiACCxoGGicvAe/fuJRR8YuuE8G4L9ZX8Rmf8epfYDXlb1IgAAAAAN/AAKTE5DT01NSVRUWP29AQIAAAAAAQGvpPZJGTuhdy8BBAaUTPPXUbi9ovdnOF1D84VQeTGZwQAAAAAAyM1NgARKAQAAAAAAACIAIBJnfJ45SYl2NzXNaajEGT+sEPKfTH0DOTjutwVMsolsSgEAAAAAAAAiACD5ydH1DonI+kmL6h1G8d2LE3a/QtFHGGI7Tw3NdHOSKF6xAAAAAAAAIgAgFg/xa71dddDa4x2BhxUP83k1YnxW8A4d+vKJpXZ0/YscqQMAAAAAACIAIF1v8STyshlqqq2Pf1VCx3ZQT0z5rT43fOifTRGlbA2EBABIMEUCIQCt+80JTKGMl91UoH4JCC0hXA7IDc++T13j0LtdJjxD2gIgOXn0G1HTbn1XlOY7ZBVSChKFw6dtALJCCgLKf1Gok6gBSDBFAiEA4x+JMSpf1V04GEHpbKUrYCjgS2OqIsbwenCMFu6RqZcCIF+tkFybjST5lwQaKCH1iBN+4m4R/AbDu72gALgIQalJAUdSIQOzuM357v/sWd8rbBxR6TKZbxoRciOMWoAjGAREJV1DiiED9Yw5sGxF6Pzb1g39D3oc5+oWvzoKfujE4fbuWt0uW6lSrjG8gyAP/AAMTE5ERUxBWUVES0VZIPa9OKssIvmrsiBNHEpCnTNwm63VLdv/fDRGg/AOJQqjEvwAD0xOUkVWT0NBVElPTktFWSECwPqivr+nKXMBUU7HZXh5/VL/fIohZZL1XqIK7SuAgnoAAQEfUMMAAAAAAAAWABRZc08j7JxLj8fRLK/R0U4FlMiQAgABAFICAAAAAV6JrzCUsTT/4+37q6ZmuLWZEt2RIAXggwsrRk/cmc8XAwAAAAAAAAAAAZDQAwAAAAAAFgAUE0foKgN7Xbs4z4xHWfJCsfXH4JoAAAAAAQEfkNADAAAAAAAWABQTR+gqA3tduzjPjEdZ8kKx9cfgmgEFGXapFBNH6CoDe127OM+MR1nyQrH1x+CaiKwiBgJ8t100sAXE659iu/LEV9djjoE+dX787I+mhnfZULY2Yhj1rML9VAAAgAEAAIAAAACAAAAAAAAAAAAAAA=='

    result = client.sign_psbt(psbt, wallet, None)
    assert len(result) == 1

    print(result[0][0], result[0][1].hex(), result[0][2].hex())
