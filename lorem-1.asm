section .data
prompt db "Hány mondatot akarsz? ",0

section .bss
inbuf: resb 4

section .data
s1: db "lorem ipsum: kockás bagoly futkorászik a paprikaerdőben.",10
len1 equ $-s1
s2: db "lorem ipsum: csendes villanykacsa suttog papucs-mantrakat.",10
len2 equ $-s2
s3: db "lorem ipsum: csokoládé tornádó táncol a kürtőskalács-szigeten.",10
len3 equ $-s3

ptrs: dq s1, s2, s3
lens: dq len1, len2, len3

section .text
global _start
_start:
    ; write prompt
    mov rax, 1
    mov rdi, 1
    lea rsi, [rel prompt]
    mov rdx, 20
    syscall

    ; read input (up to 3 chars)
    mov rax, 0
    mov rdi, 0
    lea rsi, [rel inbuf]
    mov rdx, 4
    syscall

    ; parse first digit
    lea rsi, [rel inbuf]
    mov al, [rsi]
    sub al, '0'
    cmp al, 0
    jl .default_one
    cmp al, 9
    jg .default_one
    movzx rcx, al
    cmp rcx, 0
    je .default_one
    ; rcx now count
    jmp .have_count
.default_one:
    mov rcx, 1
.have_count:

    ; loop rcx times
    xor rbx, rbx        ; loop counter increments
    xor r9, r9          ; index variable
.loop:
    ; compute index modulo 3
    mov rax, r9
    xor rdx, rdx
    mov rdi, 3
    div rdi             ; rax = r9/3, rdx = r9%3
    mov rsi, rdx        ; rsi = idx
    ; load pointer and length
    lea rdx, [rel ptrs]
    mov r10, [rdx + rsi*8]   ; pointer to string
    lea rdx, [rel lens]
    mov r11, [rdx + rsi*8]   ; length
    ; write string (syscall clobbers rcx and r11, save/restore rcx)
    push rcx
    mov rax, 1
    mov rdi, 1
    mov rsi, r10
    mov rdx, r11
    syscall
    pop rcx
    ; increment and decrement counter
    dec rcx
    inc r9
    cmp rcx, 0
    jne .loop

    ; exit
    mov rax, 60
    xor rdi, rdi
    syscall
