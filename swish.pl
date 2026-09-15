%Exercise 4
%Made by Daniel Haimov 311351647

%=== introduction ====
% Assumption: In married(X, Y), X is the male and Y is the female.
% Gender definitions
male(john).
male(michael).
male(david).
male(robert).
male(james).
female(mary).
female(susan).
female(linda).
female(karen).
female(lisa).

% Marriages
married(john, mary).
married(michael, susan).
married(david, linda).

% Parent-child relationships
parent(john, michael).
parent(mary, michael).
parent(john, lisa).
parent(mary, lisa).
parent(michael, david).
parent(susan, david).
parent(michael, karen).
parent(susan, karen).
parent(david, james).
parent(linda, james).

father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
son(X, Y) :- male(X), parent(Y, X).
daughter(X, Y) :- female(X), parent(Y, X).
grandfather(X, Y) :- male(X), parent(X, Z), parent(Z, Y).
grandmother(X, Y) :- female(X), parent(X, Z), parent(Z, Y).
grandson(X, Y) :- male(X), parent(Z, X), parent(Y, Z).
granddaughter(X, Y) :- female(X), parent(Z, X), parent(Y, Z).
siblings(X, Y) :- parent(Z, X), parent(Z, Y), X \== Y.
uncle_not_blood(X, Y) :- married(X, Z), siblings(Z, W), parent(W, Y).
cousin(X, Y) :- parent(Z, X), parent(W, Y), siblings(Z, W).
brother_in_law(X, Y) :- married(X, Z), siblings(Z, Y), male(X).
niece(X, Y) :- female(X), parent(Z, X), siblings(Z, Y).

%==== Recursion and lists ====

reverse([], []).                       % Base case: the reverse of an empty list is an empty list.
reverse([H|T], Z) :-                   % Recursive case: reverse the tail `T` and append `H` to the end.
    reverse(T, RevT), 
    append(RevT, [H], Z).

member(X, [X|_]).                      % Base case: X is the head of the list.
member(X, [_|T]) :-                    % Recursive case: check in the tail `T`.
    member(X, T).

palindrome(L) :- 
    reverse(L, L).                     % A list is a palindrome if it equals its reverse.

sorted([]).                            % An empty list is sorted.
sorted([_]).                           % A single-element list is sorted.
sorted([X,Y|T]) :-                     % Recursive case: if X <= Y, check the rest.
    X =< Y,
    sorted([Y|T]).

permutation([], []).                   % Base case: the permutation of an empty list is an empty list.
permutation([H|T], P) :-               % Recursive case: permute the tail `T`, then insert `H`.
    permutation(T, PT),
    insert(H, PT, P).

insert(X, L, [X|L]).                   % Insert `X` at the start of the list.
insert(X, [H|T], [H|NT]) :-            % Insert `X` in the tail `T`.
    insert(X, T, NT).

%==== Arithmetic ====

scum(1, 1).                                   % Base case: the sum of 1 is 1.
scum(N, Res) :-
    N > 1,
    N1 is N - 1,
    scum(N1, Res1),                           % Recursive call to sum from 1 to N-1.
    Res is Res1 + N.

sumDigits(0, 0).                              % Base case: the sum of digits of 0 is 0.
sumDigits(Num, Sum) :-
    Num > 0,
    LastDigit is Num mod 10,                  % Get the last digit.
    Rest is Num // 10,                        % Remove the last digit.
    sumDigits(Rest, SumRest),                 % Recursive call on the rest of the digits.
    Sum is SumRest + LastDigit.

split(0, []).                                 % Base case: the list for 0 is an empty list.
split(N, [Digit|Res]) :-
    N > 0,
    Digit is N mod 10,                        % Get the last digit.
    Rest is N // 10,                          % Remove the last digit.
    split(Rest, Res).

create([], 0).                                % Base case: an empty list corresponds to 0.
create([H|T], N) :-
    create(T, NT),
    N is NT * 10 + H.                         % Shift previous result by one decimal place and add the head.

reverse_number(Num, Reversed) :-
    split(Num, Digits),                       % Split `Num` into its list of digits.
    reverse(Digits, RevDigits),               % Reverse the list of digits.
    create(RevDigits, Reversed).              % Create the reversed number.

intersection([], _, []).                      % Base case: intersection with an empty list is empty.
intersection([H|T], L2, [H|Z]) :-
    member(H, L2),                            % If `H` is in `L2`, include it in the intersection.
    intersection(T, L2, Z).
intersection([_|T], L2, Z) :-
    intersection(T, L2, Z).                   % Skip `H` if it's not in `L2`.

minus([], _, []).                             % Base case: the difference with an empty list is empty.
minus([H|T], L2, Z) :-
    member(H, L2),                            % If `H` is in `L2`, skip it.
    minus(T, L2, Z).
minus([H|T], L2, [H|Z]) :-
    \+ member(H, L2),                         % If `H` is not in `L2`, include it in the result.
    minus(T, L2, Z).

















