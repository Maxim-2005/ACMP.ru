Program p0043;

var x :string;
  s, temp :integer;

Begin
  s := 0;
  temp := 0;
  
  Readln(x);
  
  For var i := 1 to length(x) do
    begin
      If Copy(x, i, 1) = '0' then
        begin
          s := s + 1;
          temp := max(temp, s);
        end
      else
        s := 0;
    end;
    Writeln(temp);
end.