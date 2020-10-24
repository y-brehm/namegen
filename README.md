# namegen

This is a nifty automatic name generation tool I use to assign names to my artist aliases, song titles and other names I use for art projects.
It's essentially a wrapper of https://github.com/sherjilozair/char-rnn-tensorflow.

Wikipedia lists of any kind are used to train on and then generate novel names inspired by that list using char-rnn. 
Results are filtered by querying the web through duckduckgo's quick answer API to validate the relative uniqueness of the generated names.

example usage:
```
bash generate-names.sh "List of legendary creatures from Japan"
```

example output:
```
Azōdamō
Iraniaa
Teōgaina
camomunn
Masokure
Keker
Nuzorogagaba
Fejake
Kamekai
Sitsuno
Temagehar
purtusuru
```

Requirements are provided in the `Dockerfile`
