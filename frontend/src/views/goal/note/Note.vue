<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <v-row justify="center">
          <v-col cols="8" lg="8" md="9" sm="11">
            <h2 class="message-title">
              Note
              <div style="display: inline;" @click="addNote">
                <v-btn
                  depressed
                  small
                  rounded
                  color="#4465c0"
                  style="color: #f0f0f0;"
                  >memo +</v-btn
                >
              </div>
            </h2>
          </v-col>
        </v-row>

        <!-- <v&#45;row> -->
        <!--   <v&#45;col> -->
        <!--     <template> -->
        <!--       <div class="text&#45;center"> -->
        <!--         <v&#45;pagination -->
        <!--           v&#45;model="page" -->
        <!--           :length="6" -->
        <!--           color="#4465c0" -->
        <!--           circle -->
        <!--         ></v&#45;pagination> -->
        <!--       </div> -->
        <!--     </template> -->
        <!--   </v&#45;col> -->
        <!-- </v&#45;row> -->

        <template>
          <v-row justify="center">
            <v-dialog width="1200" v-model="dialog">
              <Accordion>
                <div slot="source">
                  @task#23
                </div>
                <div slot="header">test test</div>
                <div slot="body">
                  <Tiptap
                    :active-buttons="[
                      'bold',
                      'italic',
                      'strike',
                      'underline',
                      'code',
                      'paragraph',
                      'h1',
                      'h2',
                      'h3',
                      'bullet_list',
                      'ordered_list',
                      'blockquote',
                      'code_block',
                      'horizontal_rule',
                      'undo',
                      'redo'
                    ]"
                  />
                </div>
              </Accordion>
            </v-dialog>
          </v-row>
        </template>

        <v-row justify="center">
          <v-col cols="6" lg="6" md="8" sm="9">
            <div v-for="note in Notes.notes" :key="note.id">
              <Accordion>
                <div slot="source">
                  @task#23
                </div>
                <div slot="header">{{ note.note_title }}</div>
                <div slot="body">
                  <Tiptap
                    :initial-content="note.note_main"
                    :active-buttons="[
                      'bold',
                      'italic',
                      'strike',
                      'underline',
                      'code',
                      'paragraph',
                      'h1',
                      'h2',
                      'h3',
                      'bullet_list',
                      'ordered_list',
                      'blockquote',
                      'code_block',
                      'horizontal_rule',
                      'undo',
                      'redo'
                    ]"
                  />
                </div>
              </Accordion>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import Accordion from "../note/Accordion";
import Tiptap from "./Tiptap.vue";

export default {
  name: "Goal",
  props: ["Notes"],

  components: {
    Accordion,
    Tiptap
  },
  data: function () {
    return {
      start_date: "2019-01-06",
      deadline: "2019-05-08",
      page: 1,
      noteList: [],
      dialog: false
    };
  },
  methods: {
    addNote: function () {
      this.dialog = true;
      console.log("ok");
    }
  }
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                           CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 100%;
  grid-template-areas: "view";
  background-color: #f0f0f0;
}

#view-area {
  grid-area: view;
}

/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  /* font-size: 34px; */
  line-height: 40px;
  color: #4465c0;
  font-size: 34px;
}

.category-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 40px;
  color: #4d4d4d;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  /* line-height: 1.6; */
  /* letter-spacing: 0.05em; */
  font-kerning: nomal;
  color: #6d6d6d;
  margin-block-end: 0em;
}

.content-splitter {
  border-block-end: solid 1px #c5c5c5;
  /* padding-bottom: 5px; */
}
.editButton {
  z-index: 50;
  position: absolute;
  right: 2%;
  top: 2%;
}

@media only screen and (max-width: 600px) {
  .message-title {
    font-size: 30px;
  }
}
</style>
