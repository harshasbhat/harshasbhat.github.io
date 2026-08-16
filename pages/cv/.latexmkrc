$pdf_mode = 5;
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %S';
$biber = 'biber %O %S';
$bibtex_use = 0;
add_cus_dep('bcf', 'bbl', 0, 'biber');
sub biber { return system("biber \"$_[0]\""); }
$success_cmd = 'true';