import gradio as gr
import os


def video_identity():
    return video

demo = gr.Interface(video_identity,
                    gr.Video(sources=['webcam']),
                    "playable_video",
                    examples=[os.path.join(os.path.dirname(__file__), "video/video_sample.mp4")],
                    cache_examples=True
                    )

if __name__ == '__main__':
    demo.launch(server_name="0.0.0.0", server_port=7860)