# 20 Newsgroups dataset

A text dataset that is useful for text classification and text clustering.


[Website](http://qwone.com/~jason/20Newsgroups/)

- approx 20,000 newsgroup documents
- from 20 different newsgroups
- Some newsgroup classes are closely related, others are very different.

**Categories:**

<table border="1">
<tbody><tr>
<td>comp.graphics<br>comp.os.ms-windows.misc<br>comp.sys.ibm.pc.hardware<br>comp.sys.mac.hardware<br>comp.windows.x</td>
<td>rec.autos<br>rec.motorcycles<br>rec.sport.baseball<br>rec.sport.hockey</td>
<td>sci.crypt<br>sci.electronics<br>sci.med<br>sci.space</td>
</tr><tr>
<td>misc.forsale</td>
<td>talk.politics.misc<br>talk.politics.guns<br>talk.politics.mideast</td>
<td>talk.religion.misc<br>alt.atheism<br>soc.religion.christian</td>
</tr>
</tbody></table>

## Download the data

The data is approx 14 MB

```sh
URL=http://qwone.com/~jason/20Newsgroups/20news-bydate.tar.gz
DATA_DIR=/home/ronny/TEMP/twenty_newsgroups/raw

wget -c $URL
tar -xvzf 20news-bydate.tar.gz

# Rename subdirectories to "train" and "test"
mv 20news-bydate-train train
mv 20news-bydate-test test
```

## Directory Structure
```
twenty_newsgroups
- train
    - alt.atheism
    - rec.autos
    - sci.space
    - comp.graphics
    - rec.motorcycles
    - soc.religion.christian
    - comp.os.ms-windows.misc
    - rec.sport.baseball
    - talk.politics.guns
    - comp.sys.ibm.pc.hardware
    - rec.sport.hockey
    - talk.politics.mideast
    - comp.sys.mac.hardware
    - sci.crypt
    - talk.politics.misc
    - comp.windows.x
    - sci.electronics
    - talk.religion.misc
    - misc.forsale
    - sci.med

- test
    - alt.atheism
    - rec.autos
    - sci.space
    - comp.graphics
    - rec.motorcycles
    - soc.religion.christian
    - comp.os.ms-windows.misc
    - rec.sport.baseball
    - talk.politics.guns
    - comp.sys.ibm.pc.hardware
    - rec.sport.hockey
    - talk.politics.mideast
    - comp.sys.mac.hardware
    - sci.crypt
    - talk.politics.misc
    - comp.windows.x
    - sci.electronics
    - talk.religion.misc
    - misc.forsale
    - sci.med
```

Within each of the category subdirectories are text files, with numeric filenames, eg:

```
- 103031
- 103114
- 103297
```

**NOTE:** The files do not have `"txt"` extensions

## Example File

Each file contains string text of an email newsgroup message, including the email header information like `To:`, `From:` `Subject:` etc, eg:

```
From: aas7@po.CWRU.Edu (Andrew A. Spencer)
Subject: Re: It's a rush... (was Re: Too fast)
Organization: Case Western Reserve University, Cleveland, OH (USA)
Lines: 38
Reply-To: aas7@po.CWRU.Edu (Andrew A. Spencer)
NNTP-Posting-Host: slc5.ins.cwru.edu


In a previous article, crh@regent.e-technik.tu-muenchen.dbp.de (Christian Huebner) says:

>brad@buck.viewlogic.com (Bradford Kellogg) writes:
>
>>I think he's talking about a different form of rush. Evidently, it's fun to be
>>terrified. But hey, if you want that kind of rush, try bobsledding. You may
>>only get up to 80 or so, but it makes 130 in a car feel like a stroll in the
>>park.
>
>Why should a good driver be terrified at 130mph? The only thing I fear
>going at 130 are drivers, who switch to the left lane without using
>either rear-view-mirror or flashers. Doing 130 to 150 ain't a rush
>for me, but it's fun and I get where I want to go much faster.
>
>But in one point You are quite right. If You are terrified at 130 You
>should better not drive that fast, or You'll be a hazard to others.
>
>BTW, before You flame me, read my E-Mail address. I know what I'm
>talking about, as I live in Germany.
>
>>- BK
>
>Chris    crh@regent.e-technik.tu-muenchen.de

not a flame, just a point:  I'd be scared at 130 here, not because i feel
_I_  or my car couldn't handle it, but because of exactly what you said:
drivers who are STUPID.  Like the ones who are doing 130 also, and so
they pull in right behind you at maybe 1-2 car lengths....oh yeah, real
smart...  This scares me in cities at 50.  When i can't see enough of
the car to make it recognizable, they are following TOO CLOSE.  And
when i see them doing this AND reading a newspaper.....*sigh*...this
is why America has 55-65 speed limits: our drivers are TOO DUMB to realise
that reading the paper should be done at breakfast, or work, not in their
car.

my thoughts..
DREW
```


