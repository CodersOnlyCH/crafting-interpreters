Nice background in the train
Amdrew
https://socrates-day.ch/
Samir Talwar
https://socrates-day.ch/
Aaron
On a Motorola 68000 you even have these as addressing modes, e.g. mov d3, (a3)+ (push) or mov -(a3), d3 (pop)
Samir Talwar
https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/
⁨Samir Talwar⁩ started
screenshare
Andreas
👍
Christian
👍
⁨Samir Talwar⁩’s
screensharehas stopped
Aaron
Was just going to mention DSPs!
Yigal
https://zspec.jaredreisinger.com/
Yigal
a slightly annotated version of the Z-Machine specification (specified after the fact)
Samir Talwar
Podcast on Infocom (ongoing, new episodes very infrequently): https://www.computerenhance.com/podcast
Yigal
oh nice
Andreas
Andrew the rest can hear him - it's a problem on your end probably
Aaron
Clang's output for both versions:
Aaron
(aarch_64)
Aaron
LBB4_12:                                ;   in Loop: Header=BB4_3 Depth=1
	ldr	x8, [x23, _vm@PAGEOFF+2064]
	ldur	d0, [x8, #-8]
	fneg	d0, d0
	stur	d0, [x8, #-8]
	b	LBB4_3
Andreas
https://godbolt.org/z/K5oMsqdjz link to godbolt
Chat
