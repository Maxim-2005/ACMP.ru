program Task;
var M1, M2, M3, Max, X:integer;
begin
read(M1, M2, M3);
 
if (M1 > 727) or (M2 > 727) or (M3 > 727) then X:=1
else if (M1 < 94) or (M2 < 94) or (M3 < 94) then X:=1
else if (M1 >= M2) and (M1 >= M3) then Max := M1
else if (M2 >= M1) and (M2 >= M3) then Max := M2
else if (M3 >= M1) and (M3 >= M2) then Max := M3;
if X=1 then write('Error') else write(Max);
 
end.