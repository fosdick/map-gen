;;Utility for Curvilinear perspective
;;Jarvis Fosdick, 10-07-05
(defun set_station ( / ss)  
(princ "\nPick View Station")
(setq view_station (getpoint))
  )
(defun Cen-p ( / )
(princ "\nPick Perspective VP (in the big circle)")
(setq big_circle (getpoint))
)
  (defun c:setbase (/ )
    (set_station)
    (cen-p)
    )

(defun c:dcp (/ )
  
  (defun d0 ( n1 n2 / )
    (cond
      ((= 0 n2)
	  (* 0 0)
       )
      ((= 0 0 )
       (/ n1 n2)
       )
      )
    )
  (defun hypt (opp adj / )
    (sqrt (+ (expt opp 2) (expt adj 2)))
    )
(defun cdx (li / )
  (car (reverse li))
  )
 (defun cdrx (li / )
   (reverse (cdr (reverse li)))
   )
(defun midpnt (p1 p2 /)
  (mapcar '+ (mapcar '(lambda (x) (/ x 2.0)) (mapcar 'dis p1 p2)) p1)
)
(defun dis (p1 p2 /)
   (- p2 p1)
)
(defun ang (opp adj /)
     (setq opp (* 1.00 opp)
	   adj (* 1.00 adj)
	   )
  (atan (d0 opp adj))
    )
(defun d->r (rads /)
  (* (/ 180 pi) rads)
)
(defun foreachss (fun ss / cnt)
  (setq cnt 0)
  (while (> (sslength ss) cnt)
    (eval '(fun (entget (ssname ss cnt))))
    (setq cnt (1+ cnt))
  )
)
(defun rlpnts (line / )
  (list (cdr (assoc 10 line)) (cdr (assoc 11 line)))
  
  )
(defun rspl (line / )
  (setq spnts '())
	(setq spnts (reverse (append spnts (rlpnts line))))
	 (setq spnts (append spnts (list (midpnt (cdx spnts)
					   (midpnt (cdx spnts) (car spnts))
					))
			     )
	       )
	(setq spnts (append spnts (list (midpnt (car spnts) (cadr spnts)))))
	 (setq spnts (append spnts (list  (midpnt (cdx spnts) (car spnts)))))
	(setq spnts (append (cdr spnts) (list (car spnts))))
	 (setq spnts spnts)
  
)
  (defun xy_zh (bas pnt /)
;(d->r (atan (/ 40 90.0)))
;(d->r (atan (/ 5.0 (hypt 50 90))))
    
  (mapcar 'd->r
	  (mapcar 'ang
		  (list (car (mapcar 'dis bas pnt)) (cdx (mapcar 'dis bas pnt)) )
		  (list (cadr (mapcar 'dis bas pnt)) (hypt (car (mapcar 'dis bas pnt)) (cadr (mapcar 'dis bas pnt))))
	  )
  )
)
(defun p-pnts (line bas /  )
  (setq pp '())
  (foreach x (rspl line)
    (setq pp (append pp (list (mapcar '+ (cdrx big_circle) (xy_zh bas x)))))
    )
  (cond
    ((and (= (length pp) 5) (car pp))
(command "spline"
(nth 0 pp)
(nth 1 pp)
(nth 2 pp)
(nth 3 pp)
(nth 4 pp)
"" "" ""
)
     )
    ((not (car pp)) (princ pp)
     ;(princ big_circle)
     )
    );cond
  )
    
  
;(foreachss (lambdarspl line_ss)

					;define view station
					;for now assume view direction on y-axis

;;simple get point
(defun getlines	(/)
  (princ "\nSelect Lines")
  (ssget)
)

(setq user_os_mode (getvar "osmode"))
  (setvar "osmode" 0)
  (cond
    ((or (not view_station) (not big_circle))
     (set_station)
     (cen-p)
     ))
(setq ss (getlines))

(foreachss (lambda (x) (p-pnts x view_station)) ss)

(setvar "osmode" user_os_mode)
  (princ)
 

);dcp
(princ "\ntype  DCP to begin")
