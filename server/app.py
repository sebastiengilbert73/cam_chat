import gradio as gr
import os
import argparse


def video_identity(video):
    return video

demo = gr.Interface(video_identity,
                    gr.Video(sources=['webcam'], include_audio=True),
                    "playable_video"
                    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--shareLink', help="Create a public url", action='store_true')
    args = parser.parse_args()

    demo.launch(server_name="0.0.0.0", server_port=7860, share=args.shareLink)
    # Cf. https://github.com/gradio-app/gradio/issues/2551