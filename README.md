<h1 align="center">Welcome to Computer Architecture :robot:</h1>
<p>
  <a href="https://twitter.com/Andrew_Brudnak" target="_blank">
    <img alt="Twitter: Andrew_Brudnak" src="https://img.shields.io/twitter/follow/Andrew_Brudnak.svg?style=social" />
  </a>
</p>

> Until now, the computer itself has been something of a mysterious black box that miraculously executes our instructions for us. This sprint will explore how computers work at a very low level, giving you additional perspective that helps you approach the software development with more confidence.

## Project

- [Implement the LS-8 Emulator](ls8/)

## Task List: add this to the first comment of your Pull Request

### Day 1: Get `print8.ls8` running

- [x] Inventory what is here
- [x] Implement the `CPU` constructor
- [x] Add RAM functions `ram_read()` and `ram_write()`
- [x] Implement the core of `run()`
- [x] Implement the `HLT` instruction handler
- [x] Add the `LDI` instruction
- [x] Add the `PRN` instruction

### Day 2: Add the ability to load files dynamically, get `mult.ls8` running

- [x] Un-hardcode the machine code
- [x] Implement the `load()` function to load an `.ls8` file given the filename
      passed in as an argument
- [x] Implement a Multiply instruction (run `mult8.ls8`)

### Day 3: Stack

- [x] Implement the System Stack and be able to run the `stack.ls8` program

### Day 4: Get `call.ls8` running

- [x] Implement the CALL and RET instructions
- [x] Implement Subroutine Calls and be able to run the `call.ls8` program

### Stretch :ghost:

- [ ] Add the timer interrupt to the LS-8 emulator
- [ ] Add the keyboard interrupt to the LS-8 emulator
- [ ] Write an LS-8 assembly program to draw a curved histogram on the screen

## Author

:octocat: **Andrew Brudnak**

- Website: http://bit.ly/made-of-stars
- Twitter: [@Andrew_Brudnak](https://twitter.com/Andrew_Brudnak)
- Github: [@brudnak](https://github.com/brudnak)

## Show your support

Give a :star2: if this project helped you!

---

_This README was generated with :sparkling_heart: by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
