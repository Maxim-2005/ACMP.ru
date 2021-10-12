Program Task4;
var X, Y:integer;
begin
Read(X,Y);
if X < Y then write('<')
else if X > Y then write('>')
else write('=');
end.