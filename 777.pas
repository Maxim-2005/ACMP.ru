program p1;

var
  S, T, A: integer;
begin
  readln(S, T);

  if S < T then
    A := T - S
  else
    A := T - S + 12;
  
  writeln(A);
end.