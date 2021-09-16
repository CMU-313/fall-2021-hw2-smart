/*!
 * Font Awesome Free 5.6.3 by @fontawesome - https://fontawesome.com
 * License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License)
 */
function hello() {
    "use strict";
    function v(c, l) {
        for (var h = 0; h < l.length; h++) {
            var z = l[h];
            z.enumerable = z.enumerable || !1,
            z.configurable = !0,
            "value"in z && (z.writable = !0),
            Object.defineProperty(c, z.key, z)
        }
    }
    function B(v) {
        for (var c = 1; c < arguments.length; c++) {
            var m = null != arguments[c] ? arguments[c] : {}
              , l = Object.keys(m);
            "function" == typeof Object.getOwnPropertySymbols && (l = l.concat(Object.getOwnPropertySymbols(m).filter(function(c) {
                return Object.getOwnPropertyDescriptor(m, c).enumerable
            }))),
            l.forEach(function(c) {
                var l, h, z;
                l = v,
                z = m[h = c],
                h in l ? Object.defineProperty(l, h, {
                    value: z,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : l[h] = z
            })
        }
        return v
    }
    function s(c, l) {
        return function(c) {
            if (Array.isArray(c))
                return c
        }(c) || function(c, l) {
            var h = []
              , z = !0
              , v = !1
              , m = void 0;
            try {
                for (var s, e = c[Symbol.iterator](); !(z = (s = e.next()).done) && (h.push(s.value),
                !l || h.length !== l); z = !0)
                    ;
            } catch (c) {
                v = !0,
                m = c
            } finally {
                try {
                    z || null == e.return || e.return()
                } finally {
                    if (v)
                        throw m
                }
            }
            return h
        }(c, l) || function() {
            throw new TypeError("Invalid attempt to destructure non-iterable instance")
        }()
    }
    function T(c) {
        V && (P ? setTimeout(c, 0) : N.push(c))
    }
    V && ((P = (n.documentElement.doScroll ? /^loaded|^c/ : /^loaded|^i|^c/).test(n.readyState)) || n.addEventListener("DOMContentLoaded", function c() {
        n.removeEventListener("DOMContentLoaded", c),
        P = 1,
        N.map(function(c) {
            return c()
        })
    }));
    function F(c) {
        if (c && V) {
            var l = n.createElement("style");
            l.setAttribute("type", "text/css"),
            l.innerHTML = c;
            for (var h = n.head.childNodes, z = null, v = h.length - 1; -1 < v; v--) {
                var m = h[v]
                  , s = (m.tagName || "").toUpperCase();
                -1 < ["STYLE", "LINK"].indexOf(s) && (z = m)
            }
            return n.head.insertBefore(l, z),
            c
        }
    }
    var I = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    function K() {
        for (var c = 12, l = ""; 0 < c--; )
            l += I[62 * Math.random() | 0];
        return l
    }
    function D(c) {
        for (var l = [], h = (c || []).length >>> 0; h--; )
            l[h] = c[h];
        return l
    }
    function W(c) {
        return c.classList ? D(c.classList) : (c.getAttribute("class") || "").split(" ").filter(function(c) {
            return c
        })
    }
    function Y(c, l) {
        var h, z = l.split("-"), v = z[0], m = z.slice(1).join("-");
        return v !== c || "" === m || (h = m,
        ~x.indexOf(h)) ? null : m
    }
    function G(c) {
        return "".concat(c).replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/'/g, "&#39;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    }
    function J(h) {
        return Object.keys(h || {}).reduce(function(c, l) {
            return c + "".concat(l, ": ").concat(h[l], ";")
        }, "")
    }
    function Q(c) {
        return c.size !== R.size || c.x !== R.x || c.y !== R.y || c.rotate !== R.rotate || c.flipX || c.flipY
    }
    function Z(c) {
        var l = c.transform
          , h = c.containerWidth
          , z = c.iconWidth
          , v = {
            transform: "translate(".concat(h / 2, " 256)")
        }
          , m = "translate(".concat(32 * l.x, ", ").concat(32 * l.y, ") ")
          , s = "scale(".concat(l.size / 16 * (l.flipX ? -1 : 1), ", ").concat(l.size / 16 * (l.flipY ? -1 : 1), ") ")
          , e = "rotate(".concat(l.rotate, " 0 0)");
        return {
            outer: v,
            inner: {
                transform: "".concat(m, " ").concat(s, " ").concat(e)
            },
            path: {
                transform: "translate(".concat(z / 2 * -1, " -256)")
            }
        }
    }
    function cc(c) {
        var l = c.icons
          , h = l.main
          , z = l.mask
          , v = c.prefix
          , m = c.iconName
          , s = c.transform
          , e = c.symbol
          , a = c.title
          , M = c.extra
          , t = c.watchable
          , f = void 0 !== t && t
          , r = z.found ? z : h
          , H = r.width
          , n = r.height
          , V = "fa-w-".concat(Math.ceil(H / n * 16))
          , i = [U.replacementClass, m ? "".concat(U.familyPrefix, "-").concat(m) : "", V].filter(function(c) {
            return -1 === M.classes.indexOf(c)
        }).concat(M.classes).join(" ")
          , o = {
            children: [],
            attributes: B({}, M.attributes, {
                "data-prefix": v,
                "data-icon": m,
                class: i,
                role: "img",
                xmlns: "http://www.w3.org/2000/svg",
                viewBox: "0 0 ".concat(H, " ").concat(n)
            })
        };
        f && (o.attributes[X] = ""),
        a && o.children.push({
            tag: "title",
            attributes: {
                id: o.attributes["aria-labelledby"] || "title-".concat(K())
            },
            children: [a]
        });
        var C, L, d, u, p, b, g, S, y, w, k, A, x, q, O, j, E, N, P, T, _, R, F, I = B({}, o, {
            prefix: v,
            iconName: m,
            main: h,
            mask: z,
            transform: s,
            symbol: e,
            styles: M.styles
        }), D = z.found && h.found ? (L = (C = I).children,
        d = C.attributes,
        u = C.main,
        p = C.mask,
        b = C.transform,
        g = u.width,
        S = u.icon,
        y = p.width,
        w = p.icon,
        k = Z({
            transform: b,
            containerWidth: y,
            iconWidth: g
        }),
        A = {
            tag: "rect",
            attributes: B({}, $, {
                fill: "white"
            })
        },
        x = {
            tag: "g",
            attributes: B({}, k.inner),
            children: [{
                tag: "path",
                attributes: B({}, S.attributes, k.path, {
                    fill: "black"
                })
            }]
        },
        q = {
            tag: "g",
            attributes: B({}, k.outer),
            children: [x]
        },
        O = "mask-".concat(K()),
        j = "clip-".concat(K()),
        E = {
            tag: "defs",
            children: [{
                tag: "clipPath",
                attributes: {
                    id: j
                },
                children: [w]
            }, {
                tag: "mask",
                attributes: B({}, $, {
                    id: O,
                    maskUnits: "userSpaceOnUse",
                    maskContentUnits: "userSpaceOnUse"
                }),
                children: [A, q]
            }]
        },
        L.push(E, {
            tag: "rect",
            attributes: B({
                fill: "currentColor",
                "clip-path": "url(#".concat(j, ")"),
                mask: "url(#".concat(O, ")")
            }, $)
        }),
        {
            children: L,
            attributes: d
        }) : function(c) {
            var l = c.children
              , h = c.attributes
              , z = c.main
              , v = c.transform
              , m = J(c.styles);
            if (0 < m.length && (h.style = m),
            Q(v)) {
                var s = Z({
                    transform: v,
                    containerWidth: z.width,
                    iconWidth: z.width
                });
                l.push({
                    tag: "g",
                    attributes: B({}, s.outer),
                    children: [{
                        tag: "g",
                        attributes: B({}, s.inner),
                        children: [{
                            tag: z.icon.tag,
                            children: z.icon.children,
                            attributes: B({}, z.icon.attributes, s.path)
                        }]
                    }]
                })
            } else
                l.push(z.icon);
            return {
                children: l,
                attributes: h
            }
        }(I), W = D.children, Y = D.attributes;
        return I.children = W,
        I.attributes = Y,
        e ? (P = (N = I).prefix,
        T = N.iconName,
        _ = N.children,
        R = N.attributes,
        F = N.symbol,
        [{
            tag: "svg",
            attributes: {
                style: "display: none;"
            },
            children: [{
                tag: "symbol",
                attributes: B({}, R, {
                    id: !0 === F ? "".concat(P, "-").concat(U.familyPrefix, "-").concat(T) : F
                }),
                children: _
            }]
        }]) : function(c) {
            var l = c.children
              , h = c.main
              , z = c.mask
              , v = c.attributes
              , m = c.styles
              , s = c.transform;
            if (Q(s) && h.found && !z.found) {
                var e = h.width / h.height / 2
                  , a = .5;
                v.style = J(B({}, m, {
                    "transform-origin": "".concat(e + s.x / 16, "em ").concat(a + s.y / 16, "em")
                }))
            }
            return [{
                tag: "svg",
                attributes: v,
                children: l
            }]
        }(I)
    }

    var hc = function() {}
      , zc = U.measurePerformance && t && t.mark && t.measure ? t : {
        mark: hc,
        measure: hc
    }
      , vc = 'FA "5.6.3"'
      , mc = function(c) {
        zc.mark("".concat(vc, " ").concat(c, " ends")),
        zc.measure("".concat(vc, " ").concat(c), "".concat(vc, " ").concat(c, " begins"), "".concat(vc, " ").concat(c, " ends"))
    }
      , sc = {
        begin: function(c) {
            return zc.mark("".concat(vc, " ").concat(c, " begins")),
            function() {
                return mc(c)
            }
        },
        end: mc
    }
      , ec = function(c, l, h, z) {
        var v, m, s, e, a, M = Object.keys(c), t = M.length, f = void 0 !== z ? (e = l,
        a = z,
        function(c, l, h, z) {
            return e.call(a, c, l, h, z)
        }
        ) : l;
        for (s = void 0 === h ? (v = 1,
        c[M[0]]) : (v = 0,
        h); v < t; v++)
            s = f(s, c[m = M[v]], m, c);
        return s
    }
      , ac = E.styles
      , Mc = E.shims
      , tc = {}
      , fc = {}
      , rc = {}
      , Hc = function() {
        var c = function(z) {
            return ec(ac, function(c, l, h) {
                return c[h] = ec(l, z, {}),
                c
            }, {})
        };
        tc = c(function(c, l, h) {
            return c[l[3]] = h,
            c
        }),
        fc = c(function(l, c, h) {
            var z = c[2];
            return l[h] = h,
            z.forEach(function(c) {
                l[c] = h
            }),
            l
        });
        var m = "far"in ac;
        rc = ec(Mc, function(c, l) {
            var h = l[0]
              , z = l[1]
              , v = l[2];
            return "far" !== z || m || (z = "fas"),
            c[h] = {
                prefix: z,
                iconName: v
            },
            c
        }, {})
    };
    function nc(c, l) {
        return tc[c][l]
    }
    Hc();
    var Vc = E.styles
      , ic = function() {
        return {
            prefix: null,
            iconName: null,
            rest: []
        }
    };
    function oc(c) {
        return c.reduce(function(c, l) {
            var h = Y(U.familyPrefix, l);
            if (Vc[l])
                c.prefix = l;
            else if (h) {
                var z = "fa" === c.prefix ? rc[h] || {
                    prefix: null,
                    iconName: null
                } : {};
                c.iconName = z.iconName || h,
                c.prefix = z.prefix || c.prefix
            } else
                l !== U.replacementClass && 0 !== l.indexOf("fa-w-") && c.rest.push(l);
            return c
        }, ic())
    }
    function Cc(c, l, h) {
        if (c && c[l] && c[l][h])
            return {
                prefix: l,
                iconName: h,
                icon: c[l][h]
            }
    }
    function Lc(c) {
        var h, l = c.tag, z = c.attributes, v = void 0 === z ? {} : z, m = c.children, s = void 0 === m ? [] : m;
        return "string" == typeof c ? G(c) : "<".concat(l, " ").concat((h = v,
        Object.keys(h || {}).reduce(function(c, l) {
            return c + "".concat(l, '="').concat(G(h[l]), '" ')
        }, "").trim()), ">").concat(s.map(Lc).join(""), "</").concat(l, ">")
    }
    var dc = function() {};
    function uc(c) {
        return "string" == typeof (c.getAttribute ? c.getAttribute(X) : null)
    }
    var pc = {
        replace: function(c) {
            var l = c[0]
              , h = c[1].map(function(c) {
                return Lc(c)
            }).join("\n");
            if (l.parentNode && l.outerHTML)
                l.outerHTML = h + (U.keepOriginalSource && "svg" !== l.tagName.toLowerCase() ? "\x3c!-- ".concat(l.outerHTML, " --\x3e") : "");
            else if (l.parentNode) {
                var z = document.createElement("span");
                l.parentNode.replaceChild(z, l),
                z.outerHTML = h
            }
        },
        nest: function(c) {
            var l = c[0]
              , h = c[1];
            if (~W(l).indexOf(U.replacementClass))
                return pc.replace(c);
            var z = new RegExp("".concat(U.familyPrefix, "-.*"));
            delete h[0].attributes.style;
            var v = h[0].attributes.class.split(" ").reduce(function(c, l) {
                return l === U.replacementClass || l.match(z) ? c.toSvg.push(l) : c.toNode.push(l),
                c
            }, {
                toNode: [],
                toSvg: []
            });
            h[0].attributes.class = v.toSvg.join(" ");
            var m = h.map(function(c) {
                return Lc(c)
            }).join("\n");
            l.setAttribute("class", v.toNode.join(" ")),
            l.setAttribute(X, ""),
            l.innerHTML = m
        }
    };
    function bc(h, c) {
        var z = "function" == typeof c ? c : dc;
        0 === h.length ? z() : (H.requestAnimationFrame || function(c) {
            return c()
        }
        )(function() {
            var c = !0 === U.autoReplaceSvg ? pc.replace : pc[U.autoReplaceSvg] || pc.replace
              , l = sc.begin("mutate");
            h.map(c),
            l(),
            z()
        })
    }
    var gc = !1;
    var Sc = null;
    function yc(c) {
        if (M && U.observeMutations) {
            var v = c.treeCallback
              , m = c.nodeCallback
              , s = c.pseudoElementsCallback
              , l = c.observeMutationsRoot
              , h = void 0 === l ? n.body : l;
            Sc = new M(function(c) {
                gc || D(c).forEach(function(c) {
                    if ("childList" === c.type && 0 < c.addedNodes.length && !uc(c.addedNodes[0]) && (U.searchPseudoElements && s(c.target),
                    v(c.target)),
                    "attributes" === c.type && c.target.parentNode && U.searchPseudoElements && s(c.target.parentNode),
                    "attributes" === c.type && uc(c.target) && ~A.indexOf(c.attributeName))
                        if ("class" === c.attributeName) {
                            var l = oc(W(c.target))
                              , h = l.prefix
                              , z = l.iconName;
                            h && c.target.setAttribute("data-prefix", h),
                            z && c.target.setAttribute("data-icon", z)
                        } else
                            m(c.target)
                })
            }
            ),
            V && Sc.observe(h, {
                childList: !0,
                attributes: !0,
                characterData: !0,
                subtree: !0
            })
        }
    }
    function wc(c) {
        for (var l = "", h = 0; h < c.length; h++) {
            l += ("000" + c.charCodeAt(h).toString(16)).slice(-4)
        }
        return l
    }
    function kc(c) {
        var l, h, z = c.getAttribute("data-prefix"), v = c.getAttribute("data-icon"), m = void 0 !== c.innerText ? c.innerText.trim() : "", s = oc(W(c));
        return z && v && (s.prefix = z,
        s.iconName = v),
        s.prefix && 1 < m.length ? s.iconName = (l = s.prefix,
        h = c.innerText,
        fc[l][h]) : s.prefix && 1 === m.length && (s.iconName = nc(s.prefix, wc(c.innerText))),
        s
    }
    var Ac = function(c) {
        var l = {
            size: 16,
            x: 0,
            y: 0,
            flipX: !1,
            flipY: !1,
            rotate: 0
        };
        return c ? c.toLowerCase().split(" ").reduce(function(c, l) {
            var h = l.toLowerCase().split("-")
              , z = h[0]
              , v = h.slice(1).join("-");
            if (z && "h" === v)
                return c.flipX = !0,
                c;
            if (z && "v" === v)
                return c.flipY = !0,
                c;
            if (v = parseFloat(v),
            isNaN(v))
                return c;
            switch (z) {
            case "grow":
                c.size = c.size + v;
                break;
            case "shrink":
                c.size = c.size - v;
                break;
            case "left":
                c.x = c.x - v;
                break;
            case "right":
                c.x = c.x + v;
                break;
            case "up":
                c.y = c.y - v;
                break;
            case "down":
                c.y = c.y + v;
                break;
            case "rotate":
                c.rotate = c.rotate + v
            }
            return c
        }, l) : l
    };
    var xc = {
        iconName: null,
        title: null,
        prefix: null,
        transform: R,
        symbol: !1,
        mask: null,
        extra: {
            classes: [],
            styles: {},
            attributes: {}
        }
    };
    function qc(c) {
        var l, h, z, v, m, s, e, a = kc(c), M = a.iconName, t = a.prefix, f = a.rest, r = (l = c.getAttribute("style"),
        h = [],
        l && (h = l.split(";").reduce(function(c, l) {
            var h = l.split(":")
              , z = h[0]
              , v = h.slice(1);
            return z && 0 < v.length && (c[z] = v.join(":").trim()),
            c
        }, {})),
        h), H = Ac(c.getAttribute("data-fa-transform")), n = null !== (z = c.getAttribute("data-fa-symbol")) && ("" === z || z), V = (m = D((v = c).attributes).reduce(function(c, l) {
            return "class" !== c.name && "style" !== c.name && (c[l.name] = l.value),
            c
        }, {}),
        s = v.getAttribute("title"),
        U.autoA11y && (s ? m["aria-labelledby"] = "".concat(U.replacementClass, "-title-").concat(K()) : m["aria-hidden"] = "true"),
        m), i = (e = c.getAttribute("data-fa-mask")) ? oc(e.split(" ").map(function(c) {
            return c.trim()
        })) : ic();
        return {
            iconName: M,
            title: c.getAttribute("title"),
            prefix: t,
            transform: H,
            symbol: n,
            mask: i,
            extra: {
                classes: f,
                styles: r,
                attributes: V
            }
        }
    }
    function Wc(c, l) {
        var h = {
            found: !1,
            width: 512,
            height: 512,
            icon: Tc
        };
        if (c && l && _c[l] && _c[l][c]) {
            var z = _c[l][c];
            h = {
                found: !0,
                width: z[0],
                height: z[1],
                icon: {
                    tag: "path",
                    attributes: {
                        fill: "currentColor",
                        d: z.slice(4)[0]
                    }
                }
            }
        } else if (c && l && !U.showMissingIcons)
            throw new Oc("Icon is missing for prefix ".concat(l, " with icon name ").concat(c));
        return h
    }
    function Yc(c) {
        var l, h, z, v, m, s, e, a, M, t = qc(c);
        return ~t.extra.classes.indexOf(Rc) ? function(c, l) {
            var h = l.title
              , z = l.transform
              , v = l.extra
              , m = null
              , s = null;
            if (p) {
                var e = parseInt(getComputedStyle(c).fontSize, 10)
                  , a = c.getBoundingClientRect();
                m = a.width / e,
                s = a.height / e
            }
            return U.autoA11y && !h && (v.attributes["aria-hidden"] = "true"),
            [c, lc({
                content: c.innerHTML,
                width: m,
                height: s,
                transform: z,
                title: h,
                extra: v,
                watchable: !0
            })]
        }(c, t) : (l = c,
        z = (h = t).iconName,
        v = h.title,
        m = h.prefix,
        s = h.transform,
        e = h.symbol,
        a = h.mask,
        M = h.extra,
        [l, cc({
            icons: {
                main: Wc(z, m),
                mask: Wc(a.iconName, a.prefix)
            },
            prefix: m,
            iconName: z,
            transform: s,
            symbol: e,
            mask: a,
            title: v,
            extra: M,
            watchable: !0
        })])
    }
    function Xc(c) {
        var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : null;
        if (V) {
            var h = n.documentElement.classList
              , z = function(c) {
                return h.add("".concat(g, "-").concat(c))
            }
              , v = function(c) {
                return h.remove("".concat(g, "-").concat(c))
            }
              , m = Object.keys(_c)
              , s = [".".concat(Rc, ":not([").concat(X, "])")].concat(m.map(function(c) {
                return ".".concat(c, ":not([").concat(X, "])")
            })).join(", ");
            if (0 !== s.length) {
                var e = D(c.querySelectorAll(s));
                if (0 < e.length) {
                    z("pending"),
                    v("complete");
                    var a = sc.begin("onTree")
                      , M = e.reduce(function(c, l) {
                        try {
                            var h = Yc(l);
                            h && c.push(h)
                        } catch (c) {
                            y || c instanceof Oc && console.error(c)
                        }
                        return c
                    }, []);
                    a(),
                    bc(M, function() {
                        z("active"),
                        z("complete"),
                        v("pending"),
                        "function" == typeof l && l()
                    })
                }
            }
        }
    }
    function Qc() {
        U.autoAddCss && !hl && (F(Gc()),
        hl = !0)
    }
    function $c(c) {
        var l = c.prefix
          , h = void 0 === l ? "fa" : l
          , z = c.iconName;
        if (z)
            return Cc(ll.definitions, h, z) || Cc(E.styles, h, z)
    }
    var cl, ll = new (function() {
        function c() {
            !function(c, l) {
                if (!(c instanceof l))
                    throw new TypeError("Cannot call a class as a function")
            }(this, c),
            this.definitions = {}
        }
        var l, h, z;
        return l = c,
        (h = [{
            key: "add",
            value: function() {
                for (var l = this, c = arguments.length, h = new Array(c), z = 0; z < c; z++)
                    h[z] = arguments[z];
                var v = h.reduce(this._pullDefinitions, {});
                Object.keys(v).forEach(function(c) {
                    l.definitions[c] = B({}, l.definitions[c] || {}, v[c]),
                    function c(l, z) {
                        var h = Object.keys(z).reduce(function(c, l) {
                            var h = z[l];
                            return h.icon ? c[h.iconName] = h.icon : c[l] = h,
                            c
                        }, {});
                        "function" == typeof E.hooks.addPack ? E.hooks.addPack(l, h) : E.styles[l] = B({}, E.styles[l] || {}, h),
                        "fas" === l && c("fa", z)
                    }(c, v[c]),
                    Hc()
                })
            }
        }, {
            key: "reset",
            value: function() {
                this.definitions = {}
            }
        }, {
            key: "_pullDefinitions",
            value: function(m, c) {
                var s = c.prefix && c.iconName && c.icon ? {
                    0: c
                } : c;
                return Object.keys(s).map(function(c) {
                    var l = s[c]
                      , h = l.prefix
                      , z = l.iconName
                      , v = l.icon;
                    m[h] || (m[h] = {}),
                    m[h][z] = v
                }),
                m
            }
        }]) && v(l.prototype, h),
        z && v(l, z),
        c
    }()), hl = !1, zl = {
        i2svg: function() {
            var c = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {};
            if (V) {
                Qc();
                var l = c.node
                  , h = void 0 === l ? n : l
                  , z = c.callback
                  , v = void 0 === z ? function() {}
                : z;
                U.searchPseudoElements && Bc(h),
                Xc(h, v)
            }
        },
        css: Gc,
        insertCss: function() {
            hl || (F(Gc()),
            hl = !0)
        },
        watch: function() {
            var c = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {}
              , l = c.autoReplaceSvgRoot
              , h = c.observeMutationsRoot;
            !1 === U.autoReplaceSvg && (U.autoReplaceSvg = !0),
            U.observeMutations = !0,
            T(function() {
                sl({
                    autoReplaceSvgRoot: l
                }),
                yc({
                    treeCallback: Xc,
                    nodeCallback: Uc,
                    pseudoElementsCallback: Bc,
                    observeMutationsRoot: h
                })
            })
        }
    }, vl = (cl = function(c) {
        var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}
          , h = l.transform
          , z = void 0 === h ? R : h
          , v = l.symbol
          , m = void 0 !== v && v
          , s = l.mask
          , e = void 0 === s ? null : s
          , a = l.title
          , M = void 0 === a ? null : a
          , t = l.classes
          , f = void 0 === t ? [] : t
          , r = l.attributes
          , H = void 0 === r ? {} : r
          , n = l.styles
          , V = void 0 === n ? {} : n;
        if (c) {
            var i = c.prefix
              , o = c.iconName
              , C = c.icon;
            return Zc(B({
                type: "icon"
            }, c), function() {
                return Qc(),
                U.autoA11y && (M ? H["aria-labelledby"] = "".concat(U.replacementClass, "-title-").concat(K()) : H["aria-hidden"] = "true"),
                cc({
                    icons: {
                        main: Jc(C),
                        mask: e ? Jc(e.icon) : {
                            found: !1,
                            width: null,
                            height: null,
                            icon: {}
                        }
                    },
                    prefix: i,
                    iconName: o,
                    transform: B({}, R, z),
                    symbol: m,
                    title: M,
                    extra: {
                        attributes: H,
                        styles: V,
                        classes: f
                    }
                })
            })
        }
    }
    ,
    function(c) {
        var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}
          , h = (c || {}).icon ? c : $c(c || {})
          , z = l.mask;
        return z && (z = (z || {}).icon ? z : $c(z || {})),
        cl(h, B({}, l, {
            mask: z
        }))
    }
    ), ml = {
        noAuto: function() {
            U.autoReplaceSvg = !1,
            U.observeMutations = !1,
            Sc && Sc.disconnect()
        },
        config: U,
        dom: zl,
        library: ll,
        parse: {
            transform: function(c) {
                return Ac(c)
            }
        },
        findIconDefinition: $c,
        icon: vl,
        text: function(c) {
            var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}
              , h = l.transform
              , z = void 0 === h ? R : h
              , v = l.title
              , m = void 0 === v ? null : v
              , s = l.classes
              , e = void 0 === s ? [] : s
              , a = l.attributes
              , M = void 0 === a ? {} : a
              , t = l.styles
              , f = void 0 === t ? {} : t;
            return Zc({
                type: "text",
                content: c
            }, function() {
                return Qc(),
                lc({
                    content: c,
                    transform: B({}, R, z),
                    title: m,
                    extra: {
                        attributes: M,
                        styles: f,
                        classes: ["".concat(U.familyPrefix, "-layers-text")].concat(r(e))
                    }
                })
            })
        },
        counter: function(c) {
            var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}
              , h = l.title
              , z = void 0 === h ? null : h
              , v = l.classes
              , m = void 0 === v ? [] : v
              , s = l.attributes
              , e = void 0 === s ? {} : s
              , a = l.styles
              , M = void 0 === a ? {} : a;
            return Zc({
                type: "counter",
                content: c
            }, function() {
                return Qc(),
                function(c) {
                    var l = c.content
                      , h = c.title
                      , z = c.extra
                      , v = B({}, z.attributes, h ? {
                        title: h
                    } : {}, {
                        class: z.classes.join(" ")
                    })
                      , m = J(z.styles);
                    0 < m.length && (v.style = m);
                    var s = [];
                    return s.push({
                        tag: "span",
                        attributes: v,
                        children: [l]
                    }),
                    h && s.push({
                        tag: "span",
                        attributes: {
                            class: "sr-only"
                        },
                        children: [h]
                    }),
                    s
                }({
                    content: c.toString(),
                    title: z,
                    extra: {
                        attributes: e,
                        styles: M,
                        classes: ["".concat(U.familyPrefix, "-layers-counter")].concat(r(m))
                    }
                })
            })
        },
        layer: function(c) {
            return Zc({
                type: "layer"
            }, function() {
                Qc();
                var l = [];
                return c(function(c) {
                    Array.isArray(c) ? c.map(function(c) {
                        l = l.concat(c.abstract)
                    }) : l = l.concat(c.abstract)
                }),
                [{
                    tag: "span",
                    attributes: {
                        class: "".concat(U.familyPrefix, "-layers")
                    },
                    children: l
                }]
            })
        },
        toHtml: Lc
    }, sl = function() {
        var c = (0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {}).autoReplaceSvgRoot
          , l = void 0 === c ? n : c;
        0 < Object.keys(E.styles).length && V && U.autoReplaceSvg && ml.dom.i2svg({
            node: l
        })
    };
    !function(c) {
        try {
            c()
        } catch (c) {
            if (!y)
                throw c
        }
    }(function() {
        f && (H.FontAwesome || (H.FontAwesome = ml),
        T(function() {
            sl(),
            yc({
                treeCallback: Xc,
                nodeCallback: Uc,
                pseudoElementsCallback: Bc
            })
        })),
        E.hooks = B({}, E.hooks, {
            addPack: function(c, l) {
                E.styles[c] = B({}, E.styles[c] || {}, l),
                Hc(),
                sl()
            },
            addShims: function(c) {
                var l;
                (l = E.shims).push.apply(l, r(c)),
                Hc(),
                sl()
            }
        })
    })
};