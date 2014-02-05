

Key Names - an experimental format for public-key fingerprints
====

Users sometimes have to compare, transcribe, and read aloud public-key fingerprints.  Typical fingerprints are hard to use:

    SSH:  43:51:43:a1:b5:fc:8b:b7:0a:3a:a9:b1:0f:66:73:a8

    GPG:  7213 5CAA EA6B 0980 126A  0371 8373 DD15 4D42 48BD

    OTR:  C4E40F71 A92175F8 597A29A7 CB7E0943 B27014FF

So we are making a format based around "psuedowords", which is hopefully easier to use:

    #1:   erocoj - igif - koziq - cfaw - nem3ak
    
    #2:   otenw5 - oxuq - 7heto - igof - ujahok

    #3:   4keqoy - aduo - sosuk - vepi - yuyoqw

In particular:
 * Base32 (RFC 4648) is chosen to help construct pseudowords
 ** This consists of 26 letters and 6 numbers.  The preference towards letters in the RFC 4648 alphabet is helpful for forming pseudowords.
 * 25 characters are grouped into pseudowords of length 6-4-5-4-6.  
 ** 25 base32 characters encodes a hash prefix of 125 bits, which is an adequate security level.
 ** The pseudowords have varying lengths to aid in detecting transcription errors.
 ** The longest pseudowords are placed at the beginning and end, since those are the most likely to be checked.
 ** No pseudowords of the same length are adjacent.  
