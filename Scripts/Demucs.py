import Scripts.AudioSeparation as AS
import Scripts.youtubeDL as ytdl
import Scripts.folder_sets as fs
import os
import shutil
import Scripts.DeleteStringForFiles as dsf

def make_kalyoke(url, dir, count, status="none"):
    output_dir=dir
    fs.SCF(output_dir)
    movie_info = ytdl.download_mp3_with_info(url, output_dir)
    ytdl.download_mp4_with_info(url, output_dir)
    movie_name = movie_info["title"]
    file_movie_name = dsf.sanitize_filename(movie_name)
    movie_id = movie_info["id"]
    movie_extractor=movie_info["extractor_key"]

    #print(f"before={movie_name}, after={after_movie_name}")
    sinput_path=f"{output_dir}/{movie_id}.mp3"
    soutput_dir=f"{output_dir}/{movie_extractor}/{count}_{file_movie_name}"
    fs.SCF(soutput_dir)
    if(not os.path.exists(f"{soutput_dir}/no_vocals.mp3")):
        AS.single_separate(sinput_path,soutput_dir,device="cuda")
        fs.rename_file(f"{soutput_dir}/htdemucs/{movie_id}/no_vocals.mp3", f"{soutput_dir}/no_vocals.mp3")
        fs.rename_file(f"{soutput_dir}/htdemucs/{movie_id}/vocals.mp3", f"{soutput_dir}/vocals.mp3")
        fs.rename_file(f"{output_dir}/{movie_id}.mp4", f"{soutput_dir}/{file_movie_name}.mp4")
        fs.rename_file(sinput_path, f"{soutput_dir}/{file_movie_name}.mp3")
        shutil.rmtree(f"{soutput_dir}/htdemucs")
    else:
        os.remove(f"{sinput_path}")
    movie_datas={
        "id": movie_id,
        "title": file_movie_name,
        "extractor": movie_extractor,
        "folder_path": f"{soutput_dir}"
    }
    return movie_datas
