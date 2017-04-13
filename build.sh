#!/bin/bash
zipped_files=(
    NEH_Grants1960s
    NEH_Grants1970s
    NEH_Grants1980s
    NEH_Grants1990s
    NEH_Grants2000s
    NEH_Grants2010s
)

mkdir -p ./xml

for grant in ${zipped_files[@]}
do
    echo "Getting grant file $grant.zip";
    wget https://securegrants.neh.gov/Open/data/$grant.zip;
    unzip -j $grant.zip $grant.xml -d xml;
    rm $grant.zip;

done

# Create SQL schema

if [ -f grants.db ]; then
    echo "grants.db file already exists. aborting...";
    exit 2;
else
    echo "Creating database and schema...\n";
    sqlite3 grants.db < schema.sql;
fi

for xml_file in ./xml/*.xml
do
    echo "Parsing XML file...";
    python parse.py $xml_file;
done


    
