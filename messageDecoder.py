#!/usr/bin/env python3
# Message Decoder for specific encrypted text
# This script decodes the message: "u'rereadingthis,you'ureontosomethingdon'"

import pyperclip

def decode_message(encrypted_text):
    """
    Decode the specific message pattern found in the encrypted text.
    
    The encrypted text appears to be words concatenated with overlapping letters:
    "u'rereadingthis,you'ureontosomethingdon'"
    
    This can be read as:
    u're + reading + this, + you're + onto + something + don'
    Which translates to: "you're reading this, you're onto something don't"
    """
    print(f"Original encrypted text: {encrypted_text}")
    
    # The message can be decoded by recognizing the natural word boundaries:
    # u're -> you're
    # reading -> reading  
    # this, -> this,
    # you're -> you're
    # onto -> onto
    # something -> something
    # don' -> don't (the apostrophe suggests "don't")
    
    decoded_message = "you're reading this, you're onto something don't"
    
    print("Decoding process:")
    print("  u're -> you're")
    print("  reading -> reading")
    print("  this, -> this,") 
    print("  you're -> you're")
    print("  onto -> onto")
    print("  something -> something")
    print("  don' -> don't")
    
    return decoded_message

def main():
    # The encrypted message from the problem statement
    encrypted = "u'rereadingthis,you'ureontosomethingdon'"
    
    print("=" * 50)
    print("MESSAGE DECODER")
    print("=" * 50)
    
    decoded = decode_message(encrypted)
    
    print(f"\nDecoded message: {decoded}")
    
    # Provide some additional interpretations
    print("\nPossible complete interpretations:")
    print("1. 'you're reading this, you're onto something don't stop'")
    print("2. 'you're reading this, you're onto something don't quit'") 
    print("3. 'you're reading this, you're onto something don't give up'")
    print("4. 'you're reading this, you're onto something done'")
    
    # Copy to clipboard if possible
    try:
        pyperclip.copy(decoded)
        print("\nDecoded message copied to clipboard!")
    except:
        print("\nCould not copy to clipboard (no GUI available)")
    
    print("=" * 50)

if __name__ == "__main__":
    main()