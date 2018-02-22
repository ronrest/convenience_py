# IMDB Movie review dataset

## Download and extract data
```sh
wget http://s3.amazonaws.com/text-datasets/aclImdb.zip

# Extract only the useful subdirectory from zip file
unzip aclImdb.zip 'aclImdb/*'

# Rename extracted subdirectory
mv aclImdb imdb_raw
```

## Directory structure

```
- imdb_raw
    - train
        - neg
            XXXX_Y.txt
            XXXX_Y.txt
            XXXX_Y.txt
            ...
        - pos
            XXXX_Y.txt
            XXXX_Y.txt
            XXXX_Y.txt
            ...

    - test
        - neg
            XXXX_Y.txt
            XXXX_Y.txt
            XXXX_Y.txt
            ...
        - pos
            XXXX_Y.txt
            XXXX_Y.txt
            XXXX_Y.txt
            ...
```


