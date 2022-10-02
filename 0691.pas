program p0691;

var
  N: integer;
  s: string;
  B: string = 'ABCEHKMOPTXY';
  H: string = '0123456789';

begin
  readln(N);
  for var i := 1 to N do
    begin
    readln(s);
    if (length(s) = 6) and
        (copy(s, 1, 1) in B) and
        (copy(s, 5, 1) in B) and
        (copy(s, 6, 1) in B) and 
        (copy(s, 2, 1) in H) and 
        (copy(s, 3, 1) in H) and 
        (copy(s, 4, 1) in H)
    then
      writeln('Yes')
    else
      writeln('No');
    end;

end.