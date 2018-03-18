/* cffi declarations for cmark */

typedef struct cmark_node cmark_node;

typedef struct cmark_mem {
  void *(*calloc)(size_t, size_t);
  void *(*realloc)(void *, size_t);
  void (*free)(void *);
} cmark_mem;

typedef void (*cmark_free_func) (cmark_mem *mem, void *user_data);

typedef struct _cmark_llist
{
  struct _cmark_llist *next;
  void         *data;
} cmark_llist;

cmark_llist * cmark_llist_append    (cmark_mem         * mem,
                                     cmark_llist       * head,
                                     void              * data);
void          cmark_llist_free_full (cmark_mem         * mem,
                                     cmark_llist       * head,
                                     cmark_free_func     free_func);
void          cmark_llist_free      (cmark_mem         * mem,
                                     cmark_llist       * head);

const char *cmark_version_string();
char *cmark_markdown_to_html(const char *text, size_t len, int options);
cmark_node *cmark_parse_document(const char *buffer, size_t len, int options);
char *cmark_render_html(cmark_node *root, int options, cmark_llist *extensions);

#define CMARK_OPT_DEFAULT 0
#define CMARK_OPT_SOURCEPOS ...
#define CMARK_OPT_HARDBREAKS ...
#define CMARK_OPT_SAFE ...
#define CMARK_OPT_NOBREAKS ...
#define CMARK_OPT_NORMALIZE ...
#define CMARK_OPT_VALIDATE_UTF8 ...
#define CMARK_OPT_SMART ...
#define CMARK_OPT_GITHUB_PRE_LANG ...
#define CMARK_OPT_LIBERAL_HTML_TAG ...
#define CMARK_OPT_FOOTNOTES ...
#define CMARK_OPT_STRIKETHROUGH_DOUBLE_TILDE ...
#define CMARK_OPT_TABLE_PREFER_STYLE_ATTRIBUTES ...