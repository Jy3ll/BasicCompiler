TEST=-45+678/43

function ds445 ( gdf , bn7)
i=0
Kao=3
while i>=0 DO
Kao=Kao+gdf*bn7 ' testowy komentarz
if Kao>1000 then
PRINT "Too much"
exit while
ELSE
PRINT Kao

end if
i=i+1
end while

print "end of test"
end function

kda=34
ds445 (65,kda)