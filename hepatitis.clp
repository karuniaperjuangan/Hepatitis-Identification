(deftemplate person
    (slot name)
    (slot age (type INTEGER))
)

(deftemplate hepatitis_evidence_count
    
    (slot HP_A_evidence_count
     (type INTEGER)
     (default 0))
    
    (slot HP_B_evidence_count
     (type INTEGER)
     (default 0))
     
     (slot HP_C_evidence_count
     (type INTEGER)
     (default 0))
     
     (slot HP_D_evidence_count
     (type INTEGER)
     (default 0))
     
     (slot HP_E_evidence_count
     (type INTEGER)
     (default 0)
     )

     (slot HP_ALCOHOLIC_evidence_count
     (type INTEGER)
     (default 0)
     )

    (slot MAX_EVIDENCE
     (type INTEGER)
     (default 0)
     )
)


; ; Evidence Finding by Condition

(defrule test_age_evidence
    (declare (salience 3))
    ?person <- (person (age ?age))
    ?evidence_count <- (hepatitis_evidence_count (HP_A_evidence_count ?a))
    (test (> ?age 55))
    =>
    (modify ?evidence_count (HP_A_evidence_count (+ ?a 3)))
    (retract ?person)
)

(defrule is_bad_sanitation
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_A_evidence_count ?a) (HP_E_evidence_count ?e))
    ?f <- (has_condition bad_sanitation)
    =>
    (modify ?evidence_count (HP_A_evidence_count (+ ?a 1)))
    (modify ?evidence_count (HP_E_evidence_count (+ ?e 1)))
    (retract ?f)
)

(defrule is_tropical
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_E_evidence_count ?e))
    ?f <- (has_condition tropical)
    =>
    (modify ?evidence_count (HP_E_evidence_count (+ ?e 2)))
    (retract ?f)
)

(defrule is_asymptomatic
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_C_evidence_count ?c))
    ?f <- (has_condition asymptomatic)
    =>
    (modify ?evidence_count (HP_C_evidence_count (+ ?c 1)))
    (retract ?f)
)

(defrule is_b_survivor
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_D_evidence_count ?d))
    ?f <- (has_condition b_survivor)
    =>
    (modify ?evidence_count (HP_D_evidence_count (+ ?d 5)))
    (retract ?f)
)

(defrule is_homosexual
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_B_evidence_count ?b) (HP_D_evidence_count ?d))
    ?f <- (has_condition homosexual)
    =>
    (modify ?evidence_count (HP_B_evidence_count (+ ?b 1)))
    (modify ?evidence_count (HP_D_evidence_count (+ ?d 1)))
    (retract ?f)
)

(defrule is_alcoholic
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_ALCOHOLIC_evidence_count ?alc))
    ?f <- (has_condition alcoholic)
    =>
    (modify ?evidence_count (HP_ALCOHOLIC_evidence_count (+ ?alc 20)))
    (retract ?f)
)

(defrule is_hemodialisis_user
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_B_evidence_count ?b) (HP_D_evidence_count ?d))
    ?f <- (has_condition hemodialisis)
    =>
    (modify ?evidence_count (HP_B_evidence_count (+ ?b 1)))
    (modify ?evidence_count (HP_D_evidence_count (+ ?d 1)))
    (retract ?f)
)

; ; Evidence Finding by Blood Test Result


(defrule have_antibody_hba
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_A_evidence_count ?a))
    ?f <- (blood_contain anti_hba)
    =>
    (modify ?evidence_count (HP_A_evidence_count (+ ?a 4)))
    (retract ?f)
)

(defrule have_antibody_hbb
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_B_evidence_count ?b))
    ?f <- (blood_contain anti_hbb)
    =>
    (modify ?evidence_count (HP_B_evidence_count (+ ?b 4)))
    (retract ?f)
)

(defrule have_antibody_hbc
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_D_evidence_count ?c))
    ?f <- (blood_contain anti_hbc)
    =>
    (modify ?evidence_count (HP_C_evidence_count (+ ?c 4)))
    (retract ?f)
)

(defrule have_antibody_hbd
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_D_evidence_count ?d))
    ?f <- (blood_contain anti_hbd)
    =>
    (modify ?evidence_count (HP_D_evidence_count (+ ?d 4)))
    (retract ?f)
)

(defrule have_antibody_hbe
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_E_evidence_count ?e))
    ?f <- (blood_contain anti_hbe)
    =>
    (modify ?evidence_count (HP_E_evidence_count (+ ?e 4)))
    (retract ?f)
)

(defrule have_alanin_transaminase
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_C_evidence_count ?c))
    ?f <- (blood_contain alanin)
    =>
    (modify ?evidence_count (HP_C_evidence_count (+ ?c 2)))
    (retract ?f)
)

(defrule have_igg
    (declare (salience 3))
    ?evidence_count <- (hepatitis_evidence_count (HP_A_evidence_count ?a) (HP_B_evidence_count ?b) (HP_C_evidence_count ?c))
    ?f <- (blood_contain igg)
    =>
    (modify ?evidence_count (HP_A_evidence_count (+ ?a 3)))
    (modify ?evidence_count (HP_B_evidence_count (+ ?b 2)))
    (modify ?evidence_count (HP_C_evidence_count (+ ?c 1)))
    (retract ?f)
)


; ; Find the maximum evidence
; ; Salience set to 1 so this rule will be fired at the end.
; ; (Other rules have salience = 2)

(defrule get_max_evidence
    (declare (salience 2))
    ?evidence_count <- (hepatitis_evidence_count (HP_ALCOHOLIC_evidence_count ?alc) (HP_A_evidence_count ?a) (HP_B_evidence_count ?b) (HP_C_evidence_count ?c) (HP_D_evidence_count ?d) (HP_E_evidence_count ?e) (MAX_EVIDENCE ?maximum)) 
    =>
    (modify ?evidence_count (MAX_EVIDENCE  (max ?a ?b ?c ?d ?e ?alc)))
)

(defrule select_max_evidence
    (declare (salience 1))
    ?evidence_count <- (hepatitis_evidence_count (HP_ALCOHOLIC_evidence_count ?alc) (HP_A_evidence_count ?a) (HP_B_evidence_count ?b) (HP_C_evidence_count ?c) (HP_D_evidence_count ?d) (HP_E_evidence_count ?e) (MAX_EVIDENCE ?maximum)) 
    =>
    (if (eq ?a ?maximum)
    then
        (retract ?evidence_count)
        (assert (disease_is hepatitis_A))
        (printout t "Hepatitis A" crlf)
    else
    (if (eq ?b ?maximum)
    then
        (retract ?evidence_count)
        (assert (disease_is hepatitis_B))
        (printout t "Hepatitis B" crlf)
    else
    (if (eq ?c ?maximum)
    then
        (retract ?evidence_count)
        (assert (disease_is hepatitis_C))
        (printout t "Hepatitis C" crlf)
    else
    (if (eq ?d ?maximum)
    then
        (retract ?evidence_count)
        (assert (disease_is hepatitis_D))
        (printout t "Hepatitis D" crlf)
    else
    (if (eq ?e ?maximum)
    then
        (retract ?evidence_count)
        (assert (disease_is hepatitis_C))
        (printout t "Hepatitis E" crlf)
    else
    (if (eq ?alc ?maximum)
    then
        (retract ?evidence_count)
        (assert (disease_is hepatitis_alcoholic))
        (printout t "Alcoholic Hepatitis" crlf)
    )
    )
    
    )
    
    )
    
    )
    
    )
    
)