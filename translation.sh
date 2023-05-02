get_inline_code() {
    line=$1

    pattern='`([^`]+)`'
    while [[ $line =~ $pattern ]]; do
        inline_codes+=("${BASH_REMATCH[1]}")
        line=${line/${BASH_REMATCH[0]}/%_inlinecode_%}
    done

    translated=$(trans -no-ansi -b en:zh-TW "$line")

    for code in "${inline_codes[@]}"; do
        translated=${translated/\%_inlinecode_\%/\`$code\`}
    done

    echo "$translated"$'\n'
}

if [[ $(git diff --name-only HEAD~1 HEAD -- README.md) ]]; then
    echo "There are changes in README.md."

    output=""
    in_code_block=0 # Track whether we're currently in a code block

    while IFS= read -r line; do
        inline_code=$(echo "$line" | awk -v RS='`' 'NR%2==0') # Extract value in inline code

        line="${line//    /%_ttab_%}" # Replace space with special character
        line=$(echo "$line" | awk 'BEGIN{FS=":";OFS=":";} {for(i=2;i<NF;i+=2) if ($i!="") $i="emoji_"$i""}1') # Replace :xxx: with :emoji_xxx:
        line="${line//./%_ddot_%}" # Replace . with special character
        line="${line//\\/%_bbackslash_%}" # Replace \ with special character

        if [[ "$line" =~ ^\<.*\> ]]; then # Ignore <tags>
            output+="$line"$'\n'

        elif [[ "$line" =~ ^\[中文版 ]]; then
            output+="$line"$'\n'

        elif [[ "$line" =~ ^# ]]; then # Ignore #
            output+="$line"$'\n'

        elif [[ "$line" =~ ^\[[^\]]*\]\(#.*\)$ ]]; then # Ignore [](#)
            output+="$line"$'\n'

        elif [[ "$line" =~ ^#+[[:space:]] ]]; then # Translate headings
            line=$(echo "$line" | sed 's/=/{EQUAL}/g')
            line=$(echo "$line" | sed -E 's/^#+[[:space:]](.*)$/#\1/')
            translated=$(get_inline_code "$line")

            output+="$translated"$'\n'

        else # Translate text
            if [[ "$line" == *"\`\`\`"* ]]; then # Ignore code blocks
                if [ $in_code_block -eq 0 ]; then
                    in_code_block=1
                else
                    in_code_block=0
                fi
                output+="$line"$'\n'
            elif [ $in_code_block -eq 1 ]; then
                output+="$line"$'\n'
            else
                translated=$(get_inline_code "$line")

                output+="$translated"$'\n'
            fi
        fi
    # Read README.md to do while
    done < README.md

    # Write output file
    echo -e "$output" > README.zh-TW.md
    sed -i 's/u003d/=/g' README.zh-TW.md
    sed -i 's/%_ttab_%/    /g' README.zh-TW.md
    sed -i 's/：/:/g' README.zh-TW.md
    sed -i 's/:emoji_/:/g' README.zh-TW.md
    sed -i 's/%_ddot_%/./g' README.zh-TW.md
    sed -i 's/%_bbackslash_%/\//g' README.zh-TW.md

fi
