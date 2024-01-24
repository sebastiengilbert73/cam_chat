import gradio as gr


def video_identity():
    return video

demo = gr.Interface(video_identity,
                    gr.Video(),
                    "playable_video"
                    )

if __name__ == '__main__':
    demo.launch(server_name="0.0.0.0", server_port=7860)