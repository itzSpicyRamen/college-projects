; Project4.asm

%include "mine.inc"

%define SYS_EXIT   1
%define SYS_OPEN  5
%define SYS_CLOSE 6
%define SYS_CREAT 8
%define SYS_READ  3
%define SYS_WRITE 4
%define STDIN     0
%define STDOUT    1
%define SYSCALL_EXIT  1

%define O_RDONLY  0
%define O_WRONLY  1
%define O_RDWR    2


%define BUFLEN   1
extern     printf
extern     fopen
extern     fprintf
extern     fclose

global main

section .data
write_char:	db 'w', 0
float_file:	dd "floats.out",0
int_file:	dd "integers.out",0
int_msg:	db "The number of integers is %d",10,0
float_msg:	db "The number of floats is %d",10,0
smallest_float:	db "The smallest float is %f",10,0
largest_float:	db "The largest float is %f",10,0
read_char:      db 'r', 0
format:         db "%f",10,0
intformat:	db "%d",10,0
filename:       dd 0
file_pointer:   dd 0
number:         dd 0
sum_int:	dd 0.0
newline:	dd 0
sum:		dd 0
ten:		dd 10
float_ten:	dd 10.0
data:		dd 0
combo:		dd 0
combo_float:	dd 0.0
string:         db "The integer is %d",10,0
neg_string:	db "The integer is -%d",10,0
sum_print:      db "The sum is %f",10,0
hasdecimal:	dd 0
isfloat:	dd 0
num_floats:	dd 0
num_ints:	dd 0
num_digits:	dd 0
small_float:	dd 0.0
large_float:	dd 0.0
hasexponent:	dd 0
exponentcount:	dd 0
zero_float:	dd 0.0
decimalcount:	dd 0

section .bss
fdwr		resd BUFLEN
fdrd		resd BUFLEN
int_desc	resd BUFLEN
float_desc	resd BUFLEN
dest		resd BUFLEN
max_num		resd BUFLEN
decimalcounter	resd 0
integer		resb 4
input		resd BUFLEN
int_sign	resd BUFLEN
exp_sign	resd BUFLEN
int_digit	resd BUFLEN
float_digit	resd BUFLEN

section .text

main:
	mov 	eax,[int_sign]
	inc 	eax
	xchg 	eax,[int_sign]
	xor	eax, eax

	mov	eax,[exp_sign]
	inc	eax
	xchg	eax,[exp_sign]
	xor	eax, eax

	mov	eax,[newline]
	mov	eax,1010b
	xchg	eax,[newline]


	;;Gets the filename
	push	dword filename
	call	GetCommandLine
	add	esp,4

	;open the file
	mov	eax, SYS_OPEN
	mov	ebx, [filename]
	mov	ecx, O_RDONLY
	mov	edx, 0700o
	int	80h

	mov	[fdrd], eax

	jmp 	FirstNum

StoreFirst:
	;read in first number
	mov	eax,[combo]
	mov	[max_num],eax
	mov	ecx,[max_num]
	
	mov     eax, 0
        mov     [combo], eax

	xor	edi, edi

	jmp	make_int_file



make_int_file:                              ;;creates the file to store the integers
	push	dword write_char
	push	dword int_file
	call	fopen
	add	esp,8
	mov	[int_desc], eax
	jmp	make_float_file

make_float_file:                            ;;creates the file to store the floats
        push    dword write_char
        push    dword float_file
        call    fopen
        add     esp,8
        mov     [float_desc], eax
        jmp     ReadFile

MakeCombo:                                 ;;multiplies the current number by 10 
	mov	eax, [combo]               ;;and adds it to the number read in 
	mov	ebx, [ten]
	mul	ebx

	mov	ebx, [data]
	add	eax, ebx
	mov	[combo], eax

	ret

MakeExponentCombo:
        mov     eax, [exponentcount]      
        mov     ebx, [ten]
        mul     ebx

        mov     ebx, [data]
        add     eax, ebx
        mov     [exponentcount], eax

        jmp	ReadFile

FirstNum:                               ;;reads the first number aka the amount of 
        mov     eax, SYS_READ           ;;numbers in the file
        mov     ebx, [fdrd]
        mov     ecx, dest
        mov     edx, BUFLEN
        int     80h


        ;read in first number
        mov     eax,[dest]
        cmp     eax, 10
        je      StoreFirst

        sub     eax,'0'

        mov     [data],eax
        mov     ecx,[data]
        call    MakeCombo

        jmp     FirstNum

ReadFile:
	mov     eax, SYS_READ
        mov     ebx, [fdrd]
        mov     ecx, dest
        mov     edx, BUFLEN
        int     80h


        ;read in first number
        mov     eax,[dest]
	cmp	eax, 10
	je	CheckFloat

	cmp 	eax, 45
	je	SetIntNeg

	cmp	eax, 43
	je	ReadFile

	cmp	eax, 46
	je	NumAfterDecimal

	cmp	eax, 69
	je	SetExponent

	mov	ebx, [hasdecimal]
	cmp	ebx, 1
	je	IncDecimalCount

	jmp	AddNum

IncDecimalCount:
        mov     ebx, [hasexponent]
        cmp     ebx, 1
        je      AddNum

	mov	ebx, [decimalcount]
	inc	ebx
	mov	[decimalcount], ebx

	jmp	AddNum

DivDecimalCount:
	fld     dword[combo_float]
        fdiv    dword[float_ten]
        fstp    dword[combo_float]

	mov	ebx, [decimalcount]
	dec	ebx
	mov	[decimalcount], ebx

	cmp	ebx, 0
	je	CheckFloatSign

	jmp	DivDecimalCount

SetExponent:
	mov	ebx, 1
	mov	[hasexponent], ebx

	mov	ebx, [isfloat]
	cmp	ebx, 0
	je	MarkFloat

	jmp	ReadFile

NumAfterDecimal:
	mov     ebx, 1
        mov     [hasdecimal], ebx
	jmp	MarkFloat

MarkFloat:
	mov	ebx, 1
	mov	[isfloat], ebx
	
	mov	ebx, [num_floats]
	inc	ebx
	mov	[num_floats], ebx

	jmp	ReadFile

AddNum:
        sub     eax,'0'

        mov     [data],eax
        mov     ecx,[data]

        mov     ebx, [hasexponent]
        cmp     ebx, 1
        je	MakeExponentCombo

        call 	MakeCombo

	mov	ebx, [num_digits]
	inc	ebx
	mov	[num_digits], ebx

	jmp	ReadFile

SetIntNeg:
	mov	ebx, [hasexponent]
	cmp 	ebx, 1
	je	SetExpNeg

	mov	ebx, 0
	mov	[int_sign], ebx
	jmp 	ReadFile

SetExpNeg:
	mov	ebx, 0
	mov	[exp_sign], ebx
	jmp	ReadFile

Negate:
	mov	edx, [combo]
	xor	eax, eax
	sub	eax, edx
	mov	[combo], edx

	jmp	Sub

CheckFloat:
	mov	ebx, [isfloat]
	cmp	ebx, 1
	je	FloatCombo

	jmp	CheckSign

FloatCombo:
	fild      dword[combo_float]
        fiadd     dword[combo]
        fstp     dword[combo_float]

	mov	ebx, [hasdecimal]
	cmp	ebx, 1
	je	DivDecimalCount

	jmp	CheckFloatSign

CheckFloatSign:
        mov     eax, [int_sign]
        cmp     eax, 0
	je	NegateFloat

	jmp	CheckExponent

NegateFloat:
        fld      dword[zero_float]
        fsub     dword[combo_float]
        fstp     dword[combo_float]

	jmp	CheckExponent

CheckExponent:
	mov	eax, [hasexponent]
	cmp	eax, 1
	je	RemoveExponent

	jmp	SetMaxMin

RemoveExponent:
	mov	ebx, [exp_sign]
	cmp	ebx, 1
	je	MulExp

	jmp	DivExp

MulExp:
	fld	dword[combo_float]
	fmul	dword[float_ten]
	fstp	dword[combo_float]

	mov	ebx, [exponentcount]
	dec	ebx
	mov	[exponentcount], ebx
	cmp	ebx, 0
	je	SetMaxMin

	jmp	MulExp

DivExp:
        fld     dword[combo_float]
        fdiv    dword[float_ten]
        fstp    dword[combo_float]

        mov     ebx, [exponentcount]
        dec     ebx
        mov     [exponentcount], ebx
        cmp     ebx, 0
	je	SetMaxMin

	jmp	DivExp

SetMaxMin:
	mov	eax, [large_float]
	cmp	eax, 0
	je	SetMax

	mov	eax, [combo_float]
	mov	ebx, [large_float]
	cmp	eax, ebx
	jg	SetMax

	jmp	MinZero

SetMax:
	fld	dword[combo_float]
	fadd	dword[zero_float]
	fstp 	dword[large_float]
	jmp	MinZero

MinZero:
	mov	eax, [small_float]
	cmp	eax, 0
	je	SetMin

	mov     eax, [combo_float]
        mov     ebx, [small_float]
        cmp     eax, ebx
        jl      SetMin

	jmp	NextLine


SetMin:
	fld     dword[combo_float]
        fadd    dword[zero_float]
        fstp    dword[small_float]
	jmp	NextLine

CheckSign:
	mov	eax, [int_sign]
	cmp	eax, 0
	je	Negate

	jmp 	Sum

IncNumInts:
	mov	ebx, [isfloat]
	cmp	ebx, 1
	je	AddToFile

	mov     ebx, [num_ints]
        inc     ebx
        mov     [num_ints], ebx
	
	jmp	AddToFile

AddToFile:
	mov	ebx, [isfloat]
	cmp	ebx, 1
	je 	AddToFloats

	jmp 	AddToInts

AddToInts:
	push	dword [combo]
	push	dword intformat
	mov	eax, [int_desc]
	push	eax
	call	fprintf
	add	esp, 12

	jmp 	NextLine

AddToFloats:
	fld     dword[combo_float]
        sub     esp,byte 8
        fstp    qword[esp]
	push	dword format
	mov	eax, [float_desc]
	push	eax
        call    printf
        add     esp,byte 12

	mov     eax, [float_desc]
        push    eax
        call    fclose

	jmp	NextLine

NextLine:
	mov	eax, BUFLEN
	mov	[exp_sign], eax

	mov     eax, BUFLEN
        mov     [int_sign], eax

	mov	eax, 0
	mov	[hasexponent], eax

	mov	eax, 0
	mov	[num_digits], eax

	mov     eax, 0
        mov     [hasdecimal], eax

	mov	eax, 0
	mov	[decimalcount], eax

	mov	eax, 0
	mov	[isfloat], eax

	mov     eax, 0
        mov     [combo], eax

	mov	eax, 0
	mov	[combo_float], eax

        add     edi, 1

	cmp	dword[max_num],edi
	jz	TotalNums

	jmp	ReadFile

Sum:
	fild	dword[sum_int]
	fiadd	dword[combo]
	fistp	dword[sum_int]

	jmp	IncNumInts

Sub:
	fild    dword[sum_int]
        fisub   dword[combo]
        fistp   dword[sum_int]

	jmp	IncNumInts

PrintSum:
	fild      dword[sum_int]
   	fstp      dword[sum_int]
	fld       dword[sum_int]            
    	sub       esp,byte 8
   	fstp      qword[esp]
   	push      dword sum_print
   	call      printf                  
   	add       esp,byte 12 

	jmp	PrintMaxMin

TotalNums:
	push    dword [num_ints]
        push    dword int_msg
        call    printf
        add     esp, 8

	push    dword [num_floats]
        push    dword float_msg
        call    printf
        add     esp, 8

	jmp	PrintSum

PrintMaxMin:
        fld      dword[large_float]
        sub      esp,byte 8
        fstp     qword[esp]
        push     dword largest_float
        call     printf
        add      esp,byte 12

	fld      dword[small_float]
        sub      esp,byte 8
        fstp     qword[esp]
        push     dword smallest_float
        call     printf
        add      esp,byte 12

	jmp 	 CloseFiles

CloseFiles:
        mov     eax, [int_desc]
        push    eax
        call    fclose

        mov     eax, [float_desc]
        push    eax
        call    fclose

	jmp	Exit

Exit:
        mov     EAX, SYSCALL_EXIT
        mov     EBX, 0
        int     080h
        ret

GetCommandLine:

        ;; Macros to move esp into ebp and push regs to be saved
         Enter 0


         Push_Regs ebx, ecx, edx

        ;; Initially sets [filename] to 0, remains 0 if there's an error
         mov ebx, [ebp + 8]
         mov [ebx], dword 0

        ;; Get argc (# of arguments)
         mov ecx, [ebp + 16]

        ;; Checks the value of argc, should be 2 (a.out and input.txt), includes the if statement m\
acro
         cmp ecx, 2
         if ne
            jmp gcl_done
         endif

	;; Get argv[0] ("a.out" or the executable, this is not used in the project)
        ;; Consult slide 6 of Stack Basics... lecture
         mov ecx, [ebp + 20]    ;  ptr to args ptr
         mov ebx, [ecx]         ;  argv[0]

        ;; Get argv[1] ("input.txt")
         mov ecx, [ebp + 20]    ; ptr to args ptr
         mov ebx, [ecx + 4]     ; argv[1]

        ;; Set the filename pointer arg on the stack to the address of the filename
         mov edx, [ebp + 8]
         mov [edx], ebx
gcl_done:
        ;; Macros to return
         Pop_Regs ebx, ecx, edx
         Leave

        ;; Return
         ret
