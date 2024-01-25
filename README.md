# Christmas Tree Kata Python

There is a shortage of Christmas trees this year, however, you can help! In the absence of real trees, Santa is going to
teach the children of the world the magic of the console.

Unfortunately, being approximately 1,751 years old, Santa can only write binary, and needs your help to write a program
in a more modern language.

## Instructions

### Input

Given the children of the world have varying screen sizes, Santa has tasked you with printing a Christmas tree to the
console for a given argument of the tree’s height to accommodate for all the children.

### Output

For example a tree with a height of 2 looks like this:

```text
 X
XXX
 |
```

And a tree with a height of 3 looks like this:

```text
  X
 XXX
XXXXX
  |
```

And a tree of height 10:

```text
         X
        XXX
       XXXXX
      XXXXXXX
     XXXXXXXXX
    XXXXXXXXXXX
   XXXXXXXXXXXXX
  XXXXXXXXXXXXXXX
 XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXX
         |
```

 

## Usage:

This setup uses _make_ and _docker_ to simplify the entire installation and usage process.

### help

Show all available _make_ commands.

```shell
make help
```

### build

Build the _docker_ container. **Run this once to start working with the project.**

```shell
make build
```

### version

Display the _Python_ version.

```shell
make version
```

### test

Run the tests.

```shell
make test
```


### coverage

Generates a code coverage report.

```shell
make coverage
```