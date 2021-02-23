from embit import script
from embit import bip32
from embit import base58

def main():    
    #Extended public key string to an address, tested against https://iancoleman.io/bip39/
    #Mnemonic used: february deposit cram leopard ripple turtle impulse history accident noodle love crazy limit pond tourist 

    #bip44, first address "124d7o3DmtXqvn1dJLxj9TQYA7v9Cmcyes" 
    key = "xpub6D2VGgnY7WJ8H3SKBPhqbarfA6uZbcUSLnuwgzE5qvmXyq23yNg42GKJgDXMJ27Q3NBeFjQDyz8Za27sYUfmWs7PNow8i3FUNwHufbyyWQK"
    
    #bip49, first address "3CntmFG5nBG9sCCr2b6MWhTAk9RLEicERn" 
    #key = "ypub6YFkZihjEjQdftpu4NwwNobdTB7eRHQjcTjyDj4hhANcj3KqXVTQuEuz1rL49NtzFLCxvnSAd4gnCG1yfWdDv1evXSrMKZfCcYQ3yR6eyP2"

    #bip84, first address "bc1qv5rgjspu3kljw8kczdvyl4x0gkk09jp7ddmrp8" 
    #key = "zpub6riY8dgyiTYHfTE3xqKscWYjZrKtwWwtc4LBfvnkqPHH9gUAC4HJrydyphFihghnGnEw5cyDDgq5iZULuheBJqJW825Cv5LCgUh7VJTTLhw"

    k = bip32.HDKey.from_base58(key)
    child = k.derive([0, 0])
    
    if key[0:4] == "xpub":
        address = script.p2pkh(child).address()
    elif key[0:4] == "zpub":
        address = script.p2wpkh(child).address()
    elif key[0:4] == "ypub":
        address = script.p2sh(script.p2wpkh(child)).address()

    print(address)

if __name__ == '__main__':
    main()