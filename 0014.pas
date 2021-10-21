program p1;

var
  a, b, N, i: integer;

begin
  
  readln(a, b);
  
  for i := 1 to a * b do
  begin
    N := a * i;
    if N mod b = 0 then
      break;
  end;
  writeln(N);
end.