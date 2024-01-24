import gradio as gr
import os


def video_identity(video):
    return video

demo = gr.Interface(video_identity,
                    gr.Video(sources=['webcam'], include_audio=True),
                    "playable_video"
                    )

if __name__ == '__main__':
    demo.launch(server_name="0.0.0.0", server_port=7860, ssl_certfile="./cert/cert.pem",
                ssl_keyfile="./cert/key.pem", ssl_verify=False)
    # Cf. https://github.com/gradio-app/gradio/issues/2551