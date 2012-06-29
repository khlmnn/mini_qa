# About `mini_qa`

`mini_qa` is a toy question-answering program.  It uses Google and
Wolfram Alpha to attempt to answer questions of the form "Who... ?"

An example question is: "Who discovered relativity?"

The design is inspired by the AskMSR system developed by researchers
at Microsoft Research.  The original paper is:

Brill, Lin, Banko, Dumais and Ng, "Data-Intensive Question
Answering" (2001).

I've described background to this program
[here](http://www.michaelnielsen.org/ddi/how-to-answer-a-question-a-simple-system/)
and
[here](http://www.michaelnielsen.org/ddi/how-to-improve-our-question-answering-system).

# Note on contributions and pull requests

Bug fixes are welcome.

This program is a toy, and I don't intend to add features, so won't
accept pull requests that add features.  But feel free to fork and add
features if you like --- the beauty of AskMSR is that it's an easy
system to extend.

If you have comments or suggestions about the style of the main
program (`mini_qa.py`), I'd like to hear them.  Leave them on the
issue tracker, or email me (mn@michaelnielsen.org).  By contast,
`test_mini_qa.py` is more of a quick-and-dirty kludge, so I'm not
looking for feedback on that code.

# Copyright and licensing

MIT License

Except the files `google.py` and `wolfram.py` all files in this
repository are copyright (c) 2012 Michael Nielsen

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
