program p1;

var N, i, S :integer;

begin
  
  readln(N);
  S := 1;
  
  for i := 1 to N do
    S := S + i;
  writeln(S);
  
end.