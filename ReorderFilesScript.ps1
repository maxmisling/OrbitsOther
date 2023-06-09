
$folderPath = "C:\Users\BSULoan\Desktop\Orbits\Assets\Orbitals\322B" #orbitals\OrbitsMesh\BackMesh100" #\Filetest" #folder path where the files are
$filePattern = "*.obj"               # obj OR txt for test

# Get the list of files in the specified folder that match the file pattern
$files = Get-ChildItem -Path $folderPath -Filter $filePattern



# Loop through each file and rename it
foreach ($file in $files) {
    #$filenameWithoutExtension = [System.IO.Path]::GetFileNameWithoutExtension($file)
    $First8 = $file.Name.Substring(0,8)

    #$extractedPart = $file.Substring(4, 2)

    $i=$First8.Substring(5)

    $j=251-$i
    $j = '{0:d3}' -f $j

    $newName = "$j.obj"# + $file.Name   # new file format obj OR txt for test
    $newPath = Join-Path -Path $folderPath -ChildPath $newName
    $file | Rename-Item -NewName $newName -Force
    Write-Host "Renamed file: $($file.Name) to $($newName)"

    Write-Host "$i"
    Write-Host "$j"
}




#(01..250) | ForEach-Object {Add-Content File$_.txt -Value "Content$_"} #test files
# gci | ren -n {[regex]::replace($_.name, '\d+', {"$args".PadLeft(4, '0')})} #zero padding
#"C:\Users\BSULoan\Desktop\orbitals\ReorderFilesScript.ps1"




