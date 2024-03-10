<div align="center"><h1>TabLLM-Copilot</h1></div>

</div>

<div align="center"><h2>Description</h2></div>

&emsp;&emsp;Powered by LLM, `TabLLM-Copilot` is able to automatically identify forms and generate corresponding data analysis and trend predictions based on questions, which helps you gain valuable insights from your data with ease. 



</div>

<div align="center"><h2>Demonstration</h2></div>

&emsp;&emsp;You can easily and directly experience the project demo online on `HuggingFace` now. Click here for Online Experience 👉 [Lesion-Cells DET - a Hugging Face Space by Tsumugii](https://huggingface.co/spaces/Tsumugii/lesion-cells-det)

</div>

<div align="center"><h2>ToDo</h2></div>

- [ ] Complete the Gradio Interface for multi-input and multi-output of the first OCR stage
- [ ] Add Dr.Wu's brief introduction
- [ ] Add a gif demonstration
- [ ] Deploy the demo on `HuggingFace`
- [ ] Finish the LLMs interface and prompt design
- [ ] Finetune opensource models for data analysis
- [ ] Try Multimodal LLM such as `LLava`





</div>

<div align="center"><h2>Quick Start</h2></div>

<details open>
    <summary><h4>Installation</h4></summary>

&emsp;&emsp;First of all, please make sure that you have already installed `conda` as Python runtime environment. And `miniconda` is strongly recommended.

&emsp;&emsp;1. create a virtual `conda` environment for the demo 😆

```bash
$ conda create -n table python==3.10 # table is the name of your environment
$ conda activate table
```

&emsp;&emsp;2. Install essential `requirements` by run the following command in the `CLI` 😊

```bash
$ git clone https://github.com/Tsumugii24/TabLLM-Copilot
$ cd TabLLM-Copilot
$ pip install -r requirements.txt
```

<details open>
    <summary><h4>Preparation</h4></summary>

&emsp;&emsp;1. open `.env.example` and fill your own `api keys` in the **corresponding place** if you want to use certain LLM, then **rename** the file to `.env`

```
openai_api_key = ""
...
```

&emsp;&emsp;2. open source LLM

```
```







</div>

<div align="center"><h2>References</h2></div>

1. [Gradio](https://www.gradio.app/)
2. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)





</div>

<div align="center"><h2>Acknowledgements</h2></div>

&emsp;&emsp;***I would like to express my sincere gratitude to Dr.Wu Yue for his invaluable guidance and supports throughout the development of this project. Wu's expertise and insightful feedback played a crucial role in shaping the direction of the project.***





</div>

<div align="center"><h2>Contact</h2></div>

Feel free to open GitHub issues or directly send me a mail if you have any questions about the project. 👻

