

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
 * Base32 (RFC 4648) is chosen to encode the public key's hash
     * This consists of 26 letters and 6 numbers.  The preference towards letters in the RFC 4648 alphabet is helpful for forming pseudowords.
 * 25 characters are grouped into pseudowords of length 6-4-5-4-6.  
     * 25 base32 characters encodes a hash prefix of 125 bits, which is an adequate security level.
     * The pseudowords have varying lengths to aid in detecting transcription errors.
     * The longest pseudowords are placed at the beginning and end, since those are the most likely to be checked.
    * No pseudowords of the same length are adjacent.  

To create a new fingerprint, we append counter values to the public key and hash the result.   The resulting hash is encoded as base32, and assigned a "score" based on how the number of consonant->vowel and vowel->consonant transitions within each pseudoword.  This process is repeated until a fingerprint is discovered with an adequate score:

    best_score =  5, iters =          1   awijft - eica - 625yb - 4w5x - rfc7jr
    best_score =  6, iters =          2   4qeigx - lwnr - rglc3 - maq5 - fiqq4t
    best_score =  7, iters =          7   wtrmob - maow - cnez2 - rczu - m4vvh2
    best_score =  9, iters =         13   3pq7j2 - ajhp - cfeij - cruv - majjog
    best_score = 10, iters =        244   aafpe5 - 2ekw - ymkey - gika - omtcee
    best_score = 11, iters =        350   kraxux - fk24 - emwas - 2qoy - bqo2he
    best_score = 12, iters =       1337   qosopd - iloz - rwxvu - znud - 7fpoar
    best_score = 13, iters =       9977   ubales - pioj - giqxi - krig - smp5ek
    best_score = 14, iters =      20852   pevexa - vtob - 3leoa - manq - kubiuv
    best_score = 15, iters =     389718   oguxs2 - ukiz - gjnur - diqe - qxihuh
    best_score = 17, iters =    1179214   erocoj - igif - koziq - cfaw - nem3ak