path=/data1

for entry in "$path"/*; do
    if [ -d "$entry" ]; then
        echo "$entry"
        cd "$entry"

        for dir in "$entry"/*; do
            if [ -d "$dir" ]; then
                echo "$dir"
                cd "$dir"

                for file in *.avi; do
                    ffmpeg -i "$file" -c:v libx264 -crf 23 -c:a copy "${file%.*}.mp4"
                done
            fi
        done
    fi
done