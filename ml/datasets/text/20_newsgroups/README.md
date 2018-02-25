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

