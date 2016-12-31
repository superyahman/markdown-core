# Markdown Core

An extensible markdown engine used in the [Markdown Plus](https://github.com/tylingsoft/markdown-plus) project.


## Installation

```
yarn add markdown-core
```


## Usage

### Node.js

```javascript
const mdc = require('markdown-core');
const html = mdc.render('# hello world');
```

### Browser

Please refer to [the example](./public).


## Delopment

### Build

```
yarn run build
```

### Verify

Host and open `public/index.html` in browser


## License

MIT


## todo

1. PPT
1. Extensions: easy to add and configure extensions. by default only core markdown features.
    1. create a class named Extension
1. get rid of ionicons because this project is not active
1. Optional
    1. change require/module.exports to import/export
1. Create a website for this project
    1. GitHub pages
