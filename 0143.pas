program p0147;

var
  N, x, x1, x2: integer;

begin
  Readln(N);
  x1 := 0;
  x2 := 1;
  for var i := 0 to N-1 do
  begin
    x := x1 + x2;
    x2 := x1;
    x1 := x;
  end;
    writeln(x);
end.