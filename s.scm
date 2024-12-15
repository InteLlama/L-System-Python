(define replace
      (lambda (x dict)
        (if (= x (car (car dict)))
          (cdr (car dict))
          (replace x (cdr dict))
        )
      )
    )
    
    (define strreplace
      (lambda (L dict)
        (if (not (null? (car (cdr L))))
          (append (replace (car L) dict) (strreplace (cdr L) dict))
          (append (replace (car L) dict) '())
        )
      )
    )
    
    (define reducelist
      (lambda (L)
        (if (not (null? (car (cdr L))))
          (append (car L) (reducelist (cdr L)))
          (append (car L) '())
        )
      )
    )
    
    (define iteration
      (lambda (L dict n)
        (if (> n 1)
          (iteration (reducelist (strreplace L dict)) dict (- n 1))
          (reducelist (strreplace L dict))
        )
      )
    )
    
    (iteration INIT (list (list 0 RULE1) (list 1 RULE2) (list 2 (list 2)) (list 3 (list 3)) (list 4 (list 4)) (list 5 (list 5))) N)