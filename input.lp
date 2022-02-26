pigeon(3). hole(4).

pigeon(X-1) :- pigeon(X), X > 1.
hole(X-1) :- hole(X), X > 1.

{assign(P,H) : hole(H)} = 1 :- pigeon(P).
:- assign(P1,H), assign(P2,H), P1 != P2.

%__opt(1,P,H) :- assign(P,H).