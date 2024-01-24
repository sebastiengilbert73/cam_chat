import gradio as gr


def video_identity():
    return video

demo = gr.Interface(video_identity,
                    gr.Video(),
                    "playable_video"
                    )

if __name__ == '__main__':
    demo.launch()