program p1;

var
  A, B, K, i: integer;

begin
  readln(A, B, K);
  
  for i := 1 to K do
      A := A mod B*10;
      
  writeln(A div B);
end.